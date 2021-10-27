from setuptools import setup


setup(
    name='cldfbench_birchall_et_al2016',
    py_modules=['cldfbench_birchall_et_al2016'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'birchall_et_al2016=cldfbench_birchall_et_al2016:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
