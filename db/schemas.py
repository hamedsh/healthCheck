SCHEMAS = {
    'api_reach': {
        "required": [
            "url",
            "method",
            "timeout"
        ],
        "properties": {
            "url": {
                "type": "string",
            },
            "method": {
                "type": "string",
                "default": "GET",
                "enum": [
                    "POST",
                    "GET"
                ],
            },
            "timeout": {
                "type": "integer",
                "default": 0,
            }
        }
    },
    'api_value': {
        "required": [
            "url",
            "method",
            "timeout",
            "check"
        ],
        "properties": {
            "url": {
                "type": "string",
            },
            "method": {
                "type": "string",
                "default": "GET",
                "enum": [
                    "POST",
                    "GET"
                ],
            },
            "timeout": {
                "type": "integer",
                "default": 0,
            },
            "check": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type":"string"
                        },
                        "value": {
                            "type": object
                        }
                    }
                }
            }
        }
    }
}
