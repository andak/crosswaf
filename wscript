top = "."

def configure(conf):
    # Configure the environment for arm
    conf.load("gcc_flags armgcc c cxx", tooldir="wafconf")

    # Target specific configuration, namely nrf52832
    cmsis = conf.path.find_node("thirdparty/cmsis")
    ld_script = cmsis.find_node("nrf52_xxaa.ld")

    target_flags = [
        "-mcpu=cortex-m4",
        "-mthumb",
        "-mabi=aapcs",
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16"
    ]

    conf.env.LINKFLAGS.extend(
        [
            # Include cmsis path to linker
            "-Wl,-L" + cmsis.path_from(conf.bldnode),
            # Tell the linker to use our custom linker script
            "-T" + ld_script.path_from(conf.bldnode)
        ]
    )
    conf.env.LINKFLAGS.extend(target_flags)

    conf.env.CPPFLAGS.append("-I" + cmsis.path_from(conf.bldnode))
    conf.env.CPPFLAGS.extend(target_flags)

    conf.env.DEFINES.append("NRF52832_XXAA")

def build(bld):
    startup = ["thirdparty/cmsis/gcc_startup_nrf52.S", "thirdparty/cmsis/system_nrf52.c"]

    # Generate elf
    bld.program(
        source = bld.path.ant_glob("src/*.c") + startup,
        target = "main.elf"
        )

    # Generate hex
    bld(source=["main.elf"], target="main.hex")
