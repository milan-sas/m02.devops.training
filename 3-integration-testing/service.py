from datastore import store_value, get_value, delete_value as ds_delete_value, list_keys


def process_and_store(key, raw_value):
    processed = raw_value.strip().upper()
    store_value(key, processed)
    return processed


def retrieve_processed(key):
    value = get_value(key)
    if value is None:
        return None
    return value.lower()


def update_value(key, raw_value):
    processed = raw_value.strip().upper()
    store_value(key, processed)
    return processed


def delete_value(key):
    return ds_delete_value(key)


def list_all_keys():
    return list_keys()
