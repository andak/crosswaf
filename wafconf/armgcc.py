from waflib.Configure import conf

# Configure waf for arm-none-eabi

@conf
def find_armgcc(conf):
    conf.find_program("arm-none-eabi-gcc", var="AS")
    conf.find_program("arm-none-eabi-ar", var="AR")
    conf.find_program("arm-none-eabi-gcc", var="LINK_CC")
    conf.find_program("arm-none-eabi-objcopy", var="OBJCOPY")
    conf.find_program("arm-none-eabi-gcc", var="CC")
    conf.find_program("arm-none-eabi-g++", var="CXX")
    conf.find_program("arm-none-eabi-c++", var="LINK_CXX")
    conf.env.CC_NAME = "armgcc"

    conf.get_cc_version(conf.env.CC, gcc=True)

def configure(conf):
    libs       = ["c", "nosys", "m"]
    c_flags    = ["-mno-unaligned-access"]
    link_flags = ["-Wl,--gc-sections", "--specs=nano.specs"]

    # configure cc for arm
    conf.load("c_config")
    conf.find_armgcc()
    conf.cc_add_flags()
    conf.link_add_flags()
    conf.load("asm")

    conf.env.ARFLAGS = ['rcs']

    conf.env.CC_TGT_F            = ['-c', '-o']
    conf.env.AS_TGT_F            = ["-c", "-o"]
    conf.env.ASLNK_TGT_F         = ["-o"]
    conf.env.CCLNK_TGT_F         = ['-o']
    conf.env.CPPPATH_ST          = '-I%s'
    conf.env.DEFINES_ST          = '-D%s'
    conf.env.LIB_ST              = '-l%s' # template for adding libs
    conf.env.LIBPATH_ST          = '-L%s' # template for adding libpaths

    conf.env.CPPFLAGS.extend(c_flags)
    conf.env.LIB          = libs
    conf.env.LINKFLAGS    = link_flags
    conf.env.CXXLNK_TGT_F = ['-o']
    conf.env.CXX_TGT_F    = ['-c', '-o']
    conf.env.CXXFLAGS     = ["-fno-exceptions"]
    conf.env.INCLUDES     = []
    conf.env.DEFINES      = []
