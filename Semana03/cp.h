#ifndef CP_H
#define CP_H

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>


int comparation(char *full,char *unfinished);
int copyPaste(char *oldArq,char *newArq);
int cpComplete(char type,char *copy,char *R,char *paste);
void cpRedirector(char *command);

#endif
