# Tell waf to use CC for compiling C source files.

# This a slight modification of the original source: waflib/Tools/c.py;
# do not use absolute paths in the "run_str" variable.
# This makes waf compatible with arm-none-eabi and cygwin.
# Using absolute paths in cygwin breaks the compilation, because arm-none-eabi-gcc
# expects windows file paths (e.g. C:\repo) not cywgin paths (/home/anders/repo).
# See https://bugs.launchpad.net/gcc-arm-embedded/+bug/1282943

from waflib import TaskGen, Task
from waflib.Tools import c_preproc
from waflib.Tools.ccroot import link_task, stlink_task

@TaskGen.extension('.c')
def c_hook(self, node):
	"Binds the c file extensions create :py:class:`waflib.Tools.c.c` instances"
	if not self.env.CC and self.env.CXX:
		return self.create_compiled_task('cxx', node)
	return self.create_compiled_task('c', node)

class c(Task.Task):
	"Compiles C files into object files"
	run_str = '${CC} ${ARCH_ST:ARCH} ${CFLAGS} ${FRAMEWORKPATH_ST:FRAMEWORKPATH} ${CPPPATH_ST:INCPATHS} ${DEFINES_ST:DEFINES} ${CC_SRC_F}${SRC} ${CC_TGT_F}${TGT} ${CPPFLAGS}'
	vars    = ['CCDEPS'] # unused variable to depend on, just in case
	ext_in  = ['.h'] # set the build order easily by using ext_out=['.h']
	scan    = c_preproc.scan

class cprogram(link_task):
	"Links object files into c programs"
	run_str = '${LINK_CC} ${LINKFLAGS} ${CCLNK_SRC_F}${SRC} ${CCLNK_TGT_F}${TGT} ${RPATH_ST:RPATH} ${FRAMEWORKPATH_ST:FRAMEWORKPATH} ${FRAMEWORK_ST:FRAMEWORK} ${ARCH_ST:ARCH} ${STLIB_MARKER} ${STLIBPATH_ST:STLIBPATH} ${STLIB_ST:STLIB} ${SHLIB_MARKER} ${LIBPATH_ST:LIBPATH} ${LIB_ST:LIB} ${LDFLAGS}'
	ext_out = ['.bin']
	vars    = ['LINKDEPS']
	inst_to = '${BINDIR}'

class cstlib(stlink_task):
	"Links object files into a c static libraries"
	pass # do not remove

TaskGen.declare_chain(
    "hex",
    rule = "${OBJCOPY} -O ihex ${SRC} ${TGT}",
    ext_in = ".elf",
    ext_out = ".hex",
)
