#include<stdio.h>

int main(){
    char string[100];
    scanf("%[^\n]s",&string);
    int i=0;
    while(string[i])i++;
    int n=i,j=i-1;
    for(i=0;i<n/2;i++){
        if(string[i]!=string[j--])break;
    }
    if(i>=j){
        printf("Palindrome");
    }else{
        printf("Not Palindrome");
    }
    // printf("%s %d %d",string,i,j);
}