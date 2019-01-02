/* Linker script to configure memory regions. */

GROUP(-lgcc -lc -lnosys)

MEMORY
{
  /* The flash size is really 512K, but we
   *  use the last page (4K) for permanent storage. */
  FLASH (rx) : ORIGIN = 0x00000000, LENGTH = (512K - 4K)
  RAM (rwx) :  ORIGIN = 0x20000000, LENGTH = 64K
}

INCLUDE "common.ld"
