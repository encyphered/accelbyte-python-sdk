### Usage

##### Shorthand method

    import gpp

    gpp.initialize()
    await gpp.send_metric(event_name, payload_dict, event_timestamp='2021-10-25T03:14:15.000Z')

##### Longer method using low-level SDK

    import accelbyte_py_sdk
    from accelbyte_py_sdk.api.amalgam_game_telemetry import TelemetryBody
    from accelbyte_py_sdk.api.amalgam_game_telemetry import \
        protected_save_events_game_telemetry_v1_protected_events_post_async
    from accelbyte_py_sdk.api.iam import token_grant_v3_async

    accelbyte_py_sdk.initialize()
    await token_grant_v3_async(grant_type="client_credentials")

    telemetry = TelemetryBody.create(event_name, event_namespace, payload, event_timestamp=event_timestamp)
    await protected_save_events_game_telemetry_v1_protected_events_post_async(telemetry)
