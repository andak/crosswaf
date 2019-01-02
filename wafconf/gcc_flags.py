from waflib.Configure import conf

# Add misc gcc flags

common_flags = [
    # Generate debug symbols
    "-ggdb3",
    # Keep each function in a separate section, so the linker can discard unused ones
    "-ffunction-sections",
    "-fdata-sections",
    "-fno-strict-aliasing",
    "-fdiagnostics-color",

    # Thank you SO. https://stackoverflow.com/a/3376483
    # Those marked * sometimes give too many spurious warnings,
    # so I use them on as-needed basis. C essential.

    ### This section contains the warnings usually coming from  "-Wall",
    "-Waddress",
    "-Warray-bounds=1",
    "-Wbool-compare",
    "-Wbool-operation",
    "-Wchar-subscripts",
    "-Wcomment",
    "-Wenum-compare",
    "-Wformat",
    "-Wint-in-bool-context",
    "-Winit-self",
    "-Wlogical-not-parentheses",
    "-Wmaybe-uninitialized",
    "-Wmemset-elt-size",
    "-Wmemset-transposed-args",
    "-Wmisleading-indentation",
    "-Wno-attributes",
    "-Wmissing-braces",
    "-Wnarrowing",
    "-Wnonnull",
    "-Wnonnull-compare",
    "-Wopenmp-simd",
    "-Wparentheses",
    "-Wrestrict",
    "-Wreturn-type",
    "-Wsequence-point",
    "-Wsign-compare",
    "-Wsizeof-pointer-memaccess",
    "-Wstrict-aliasing",
    "-Wstrict-overflow=1",
    "-Wswitch",
    "-Wtautological-compare",
    "-Wtrigraphs",
    "-Wuninitialized",
    "-Wunused-label",
    "-Wunused-value",
    "-Wunused-variable",
    "-Wvolatile-register-var",

    ### This section contains the warnings usually coming from -Wextra
    "-Wclobbered",
    "-Wempty-body",
    "-Wignored-qualifiers",
    "-Wimplicit-fallthrough=3",
    "-Wmissing-field-initializers",
    "-Wsign-compare",
    "-Wtype-limits",
    "-Wuninitialized",
    "-Wshift-negative-value",
    "-Wunused-parameter",
    "-Wunused-but-set-parameter",

    ### Other warnings
    # useful because usually testing floating-point numbers for equality is bad.
    "-Wfloat-equal",
    # warn whenever a local variable shadows another local variable,
    # parameter or global variable or whenever a built-in function is shadowed.
    "-Wshadow",
    # warn if anything depends upon the size of a function or of void.
    "-Wpointer-arith",
    # warns about cases where the compiler optimizes based on the assumption
    # that signed overflow does not occur. (The value 5 may be too strict, see the manual page.)
    "-Wstrict-overflow=5",
    # give string constants the type const char[length] so that copying
    # the address of one into a non-const char * pointer will get a warning.
    "-Wwrite-strings",
    # warn whenever a pointer is cast to remove a type qualifier from the target type*.
    "-Wcast-qual",
    # warn whenever a switch statement has an index of enumerated type
    # and lacks a case for one or more of the named codes of that enumeration*.
    "-Wswitch-enum",
    # warn if the compiler detects that code will never be executed*.
    "-Wunreachable-code",
]

@conf
def add_gcc_flags(conf):
    conf.env.CPPFLAGS = common_flags
    conf.env.ASFLAGS = common_flags
    conf.env.CFLAGS = ["-std=c11"]
    conf.env.CXXFLAGS = ["-std=c++17"]

def configure(conf):
    conf.add_gcc_flags()
