# Cross compiling with waf
A template for cross compilation.

This example targets the ARM-based [nrf52832] but can easily be modified to support other targets.


### Prerequisites

* python
* [arm-none-eabi]


### Usage

```sh
$ ./waf configure
Setting top to                           : /home/anders/repo/crosswaf
Setting out to                           : /home/anders/repo/crosswaf/build
Checking for program 'arm-none-eabi-gcc' : /usr/bin/arm-none-eabi-gcc
Checking for program 'arm-none-eabi-ar'  : /usr/bin/arm-none-eabi-ar
Checking for program 'arm-none-eabi-gcc' : /usr/bin/arm-none-eabi-gcc
Checking for program 'arm-none-eabi-objcopy' : /usr/bin/arm-none-eabi-objcopy
Checking for program 'arm-none-eabi-gcc'     : /usr/bin/arm-none-eabi-gcc
Checking for program 'arm-none-eabi-g++'     : /usr/bin/arm-none-eabi-g++
Checking for program 'arm-none-eabi-c++'     : /usr/bin/arm-none-eabi-c++
'configure' finished successfully (0.048s)
$ ./waf
Waf: Entering directory `/home/anders/repo/crosswaf/build'
[1/5] Compiling thirdparty/cmsis/system_nrf52.c
[2/5] Compiling thirdparty/cmsis/gcc_startup_nrf52.S
[3/5] Compiling src/main.c
[4/5] Linking build/main.elf
[5/5] Compiling build/main.elf
Waf: Leaving directory `/home/anders/repo/crosswaf/build'
'build' finished successfully (0.170s)
```

[nrf52832]: https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF52832
[arm-none-eabi]: https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads
