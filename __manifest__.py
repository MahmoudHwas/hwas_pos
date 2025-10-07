{
    'name': ' POS Custom Features',
    'depends': [
        'point_of_sale',
        'hr',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
'views/invoice_document_view.xml',
        'views/pos_view.xml',


    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'hwas_pos/static/src/overrides/models/*.js',
            'hwas_pos/static/src/js/**/*.js',
            'hwas_pos/static/src/xml/**/*.xml',
            'hwas_pos/static/src/css/**/*.scss',  # optional
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
