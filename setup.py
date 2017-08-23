from distutils.core import setup

setup(
    name='t80s_reduce',
    version='0.0.1',
    packages=['t80s_reduce', 't80s_reduce.core', 't80s_reduce.util','t80s_reduce.t80s_process',
              't80s_reduce.t80s_check_calibrations', 't80s_reduce.t80s_sort_night', 't80s_reduce.t80s_sort_data',
              't80s_reduce.t80s_gen_download', 't80s_reduce.t80s_sort_calibrations'],
    url='https://github.com/tribeiro/t80s_reduce/',
    license='BSD',
    author='Tiago Ribeiro de Souza',
    author_email='tribeiro@ufs.br',
    description='An image reducer for robotic telescopes',
    install_requires=['astropy',
                      'colorlog',
                      'ccdproc>=0.3.3',
                      'pyyaml',
                      'fits_reduce',
],
    dependency_links=['https://github.com/tribeiro/fits_reduce/archive/master.zip'],
    scripts=['scripts/t80s_check_calibrations','scripts/t80s_gen_download','scripts/t80s_process',
             'scripts/t80s_sort_calibrations', 'scripts/t80s_sort_night', 'scripts/t80s_sort_data']
)
