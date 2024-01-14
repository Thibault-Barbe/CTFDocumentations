#include <stdlib.h>
#include <unistd.h>

int main(void)
{
   setreuid(1155, 1155); // 0 is root, might need to be modified for your user
   system("/bin/bash");

   return 0;
}

