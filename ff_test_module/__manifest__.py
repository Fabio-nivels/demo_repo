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
        ]
    },
    'data': [
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/images/image1.png'
    ],
}
