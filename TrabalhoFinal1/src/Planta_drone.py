#Augusto Perez de Andrade 11611EMT009
#Larrisa Teodoro da Silva 11321EMT021 
#Luiz da Silva Moura 11611EMT028
#Matheus Santana de Aráujo 11611EMT026
#Pedro Henrique Silva Oliveira 11611EMT007

import numpy as np

#responsavel pelo calculo do do comportamento real do drone
class Planta:
    # contrutor que inicializa todos os parametros utilizado na simulação
    def __init__(self , t):
        # Parâmetros de simulação
        self.h = t # passo da simulação de tempo continuo
        self.Ts = t *10  # intervalo de atuação do controlador
        self.tc = 0 # tempo execução  da planta 
        self.td = 0# tempo execução  do controlador
        self.x = np.zeros(8) # vetor de estados do drone x = [w r_xy v_xy phi omega]
        self.k = 0
        self.u = np.zeros(2) # comando de controle

        self.m = 0.25  # massa
        self.g = 9.81  # aceleração da gravidade
        self.l = 0.1  # tamanho
        self.kf = 1.744e-08  # constante de força
        self.Iz = 2e-4  # momento de inércia
        self.tal = 0.005
        self.Fg = np.array([[0],
                            [-self.m * self.g]])


        self.phi_max = 15 * np.pi / 180.  # ângulo máximo
        self.w_max = 15000
        self.Fc_max = self.kf * self.w_max**2  # força de controle máxima
        self.Tc_max = self.l * self.kf * self.w_max**2

        self.correct = False
    # RETORNA SE JA CHEGOU NO PONTO
    def GetToPoint(self):
        return self.correct

    def SetToPoint(self, sp):
        self.correct = sp
    
    def rk4(self, tk, h, xk, uk):
        k1 = self.x_dot(tk, xk, uk)
        k2 = self.x_dot(tk + h / 2.0, xk + h * k1 / 2.0, uk)
        k3 = self.x_dot(tk + h / 2.0, xk + h * k2 / 2.0, uk)
        k4 = self.x_dot(tk + h, xk + h * k3, uk)

        return xk + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    # x = [w r_xy v_xy phi omega]'
    def x_dot(self, t, x, w_):
        # Estados atuais
        w = x[0:2]
        r = x[2:4]
        v = x[4:6]
        phi = x[6]
        ome = x[7]

        # Variáveis auxiliares
        # Forças
        f1 = self.kf * w[0]**2
        f2 = self.kf * w[1]**2
        # Torque
        Tc = self.l * (f1 - f2)
        # Força de controle
        Fc_B = np.array([[0],
                        [(f1 + f2)]])
        # Matriz de atitude
        D_RB = np.array([[np.cos(phi), -np.sin(phi)],
                        [np.sin(phi), np.cos(phi)]])

        # Derivadas
        w_dot = (-w + w_) / self.tal
        r_dot = v
        v_dot = (1 / self.m) * (D_RB @ Fc_B + self.Fg)
        v_dot = v_dot.reshape(2,)
        phi_dot = np.array([ome])
        ome_dot = np.array([Tc / self.Iz])

        return np.concatenate([w_dot,
                               r_dot,
                               v_dot,
                               phi_dot,
                               ome_dot])
    #parametro de entrada ponto desejado 
    def GsxCs(self, r_):#G(s)*c(s)
        if (self.k % (self.Ts / self.h)) == 0:
            r_k = self.x[2:4]
            v_k = self.x[4:6]
            phi_k = self.x[6]
            ome_k = self.x[7]

            v_ = np.array([0, 0])

            # Controle de posição
            kpP = np.array([0.075])
            kdP = np.array([0.25])

            eP = r_ - r_k
            eV = v_ - v_k

            if np.linalg.norm(eP) < .1 :
                self.correct = True

            Fx = kpP * eP[0] + kdP * eV[0]
            Fy = kpP * eP[1] + kdP * eV[1] - self.Fg[1]
            Fy = np.maximum(0.2 * self.Fc_max, np.minimum(Fy, 0.8 * self.Fc_max))

            # Controle de Atitude
            phi_ = np.arctan2(-Fx, Fy)

            if np.abs(phi_) > self.phi_max:
                signal = phi_ / np.absolute(phi_)
                phi_ = signal * self.phi_max
                # Limitando o ângulo
                Fx = Fy * np.tan(phi_)

            Fxy = np.array([Fx, Fy])
            Fc = np.linalg.norm(Fxy)
            f12 = np.array([Fc / 2.0, Fc / 2.0])

            # Constantes Kp e Kd
            kpA = np.array([0.75])
            kdA = np.array([0.05])

            ePhi = phi_ - phi_k
            eOme = 0 - ome_k

            Tc = kpA * ePhi + kdA * eOme
            Tc = np.maximum(-0.4 * self.Tc_max, np.minimum(Tc, 0.4 * self.Tc_max))

            # Delta de forças

            df12 = np.absolute(Tc) / 2.0
            if (Tc >= 0.0):
                f12[0] = f12[0] + df12
                f12[1] = f12[1] - df12
            else:
                f12[0] = f12[0] - df12
                f12[1] = f12[1] + df12

            # Limitadores
            w1_ = np.sqrt(f12[0] / (self.kf))
            w2_ = np.sqrt(f12[1] / (self.kf))

            # Limitando o comando do motor entre 0 - 15000 rpm
            w1 = np.maximum(0., np.minimum(w1_, self.w_max))
            w2 = np.maximum(0., np.minimum(w2_, self.w_max))

            # Determinação do comando de entrada
            self.u = np.array([w1, w2])

        # Simulação um passo a frente
        self.x = self.rk4(self.tc, self.h, self.x, self.u)
        self.tc = self.tc +self.h
        self.k += 1

        return self.x[2],self.x[3] ,self.x[6]


    
