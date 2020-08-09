QUERIES = {
    'add_service':
        'insert into services(name, type, metadata, status) values("{name}", {type}, "{metadata}", 1)',
    'services_last_row_id': 'select max(id) from services',
    'get_active_services': 'select services.id, services.name, services.type, service_types.Type, services.metadata from services INNER join service_types on services.type = service_types.id',
    'get_active_services_type': 'select services.id, services.name, services.type, service_types.Type, services.metadata from services INNER join service_types on services.type = service_types.id where services.type = {}'

}
