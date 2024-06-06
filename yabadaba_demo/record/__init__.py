from yabadaba import recordmanager

# Manually install records to recordmanager
recordmanager.import_style('faq', '.faq', __name__, 'FAQ')
recordmanager.import_style('demo', '.demo', __name__, 'Demo')
recordmanager.import_style('bad_record', '.bad_record', __name__, 'BadRecord')