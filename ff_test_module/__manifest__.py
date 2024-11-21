{
    'name': 'FF Test Module',
    'version': '16.0.11.24.01',
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
        'views/my_model.xml',
        'views/sale_order.xml',
        'templates/sale_order.xml',
        'data/my_model_data.xml',
        'views/res_partner.xml',
        'templates/hello_world.xml',
        'wizard/wizard.xml'
    ],
    'images': [
        'static/description/images/image1.png'
    ],
}
