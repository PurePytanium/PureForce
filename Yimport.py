def Yimport(Module):
    def Procceed(Method):
        return str(input('{} is not installed. Install({})? [Y/N]> ' \
                         .format(Module, Method)))
    def Get_Module(Method, Args):
        import subprocess as sp
        sp.call(
            'python -m {} {} {}'.format(Method, Args, Module),
            shell = True,
            creationflags=0x08000000)
    try: return __import__(Module)
    except Exception:
        if Procceed('pip').lower().startswith('n'):
            print('{} Installation Aborted'.format(Module))
            return False
        Get_Module('pip install', '-q --isolate')
        try:
            Module = __import__(Module)
            print('Installation Completed using pip')
            return Module
        except Exception:
            if Procceed('easy_install').lower().startswith('n'):
                print('{} Installation Aborted'.format(Module))
                return False
            Get_Module('easy_install', '-q')
            try:
                Module = __import__(Module)
                print('Installation Completed using easy_install')
                return Module
            except Exception as Error:
                print('Installation Failed ; {}'.format(Error))
                return False
