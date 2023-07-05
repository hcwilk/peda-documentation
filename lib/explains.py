

## Compilation Security Measures

relro = """Read-only relocations (RELRO) is a feature that helps harden your binaries against certain types of exploits. If RELRO is enabled, the relocation sections are made read-only.  
If an attacker is able to overflow a buffer and overwrite a function's GOT entry, the system will not allow this to be written due to the memory protections and the program will crash instead.""" 
canary = """ Stack canaries or stack cookies are a way to protect the stack from buffer overflows. A canary is a random value placed on the stack right before the return pointer. When a function returns, it 
checks to see if the canary value has changed. If the canary value is different, the program will abort, as a changed canary value suggests a buffer overflow has occurred, overwriting the canary."""

nx = """The No-eXecute (NX) bit makes certain areas of memory non-executable, meaning that even if attacker-controlled code is written to a certain area of memory, it cannot be executed.
It provides a mitigation against certain types of exploits, such as arbitrary code execution exploits. """

pie = """Position Independent Executable (PIE) is a property of a binary which allows it to be loaded into any location of memory and executed. This is used in combination with a feature called 
Address Space Layout Randomization (ASLR), which randomly arranges the address space positions of key data areas of a program, to help prevent an attacker from predicting target addresses. """

fortify = """_FORTIFY_SOURCE is a macro in GNU C Library that provides compile-time and runtime buffer overflow checks.
This can catch buffer overflows before they lead to arbitrary code execution or other attacks."""




## Explanations Dictionary to be imported
explanations = {
        "relro":relro,
        "canary": canary,
        "nx":nx, 
        "pie":pie,
        "fortify":fortify
    }
