{
    'name': 'FF Test Module',
    'version': '17.0.11.24.01',
    'category': 'Accounting/Accounting',
    'description': """""",
    'depends': [
        'sale',
        'website'
    ],

    'assets': {
        'web.report_assets_common': [
            'ff_test_module/static/src/scss/my_model.scss'
        ],
        'web.assets_backend': [
            'ff_test_module/static/src/scss/style.css'
        ]
    },
    'data': [
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/images/image1.png'
    ],
}
