{
    'name': 'Demo Module',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """""",
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'sale',
        'website'
    ],

    'assets': {
        'web.report_assets_common': [
            'demo_module/static/src/scss/my_model.scss'
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
}
