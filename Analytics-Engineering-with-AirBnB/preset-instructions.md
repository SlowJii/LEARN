# Preset Instructions

## SQLAlchemy URL
```
snowflake://preset@aacolqm-cw70810/AIRBNB?role=REPORTER&warehouse=COMPUTE_WH
```

## Security JSON
```json
{
    "auth_method": "keypair",
    "auth_params": {
        "privatekey_body": "-----BEGIN ENCRYPTED PRIVATE KEY-----\nMIIFNTBfBgkqhkiG9w0BBQ0wUjAxBgkqhkiG9w0BBQwwJAQQ17eYL+l/orKE7Eg2\nWPclZQICCAAwDAYIKoZIhvcNAgkFADAdBglghkgBZQMEASoEEAhGo7yHFSed+8/C\nY3V3L+0EggTQjuS7gXiHbOhNMIsSVl5+oIIF36SUMg52wdQb2x+lLQw/fYzbTc+S\n+H96votkvlObd3qLa/ZP1/Eb+tO8dOln6jMAl+l4GCWjspTQ4Km5h6Sj8hlaBbB2\nancUJUhwY6it1Eoe4JHrgArQeMriD6VsftTmomplSMoZ7OjhxxpiSJqqd/eIwyEy\naD5ZB0+Ki7qmyKkuMGYkvNle74XM9wQruo4AiKpU8ONEnsLAewZkX6huwlgEOHQ4\nFE2plGXMg16O3P0xKOb2N2sZpmU/l52tgtCZL+9eZQoSCzWnRGXce6tvuhTj6kII\nQra3Co5jlbExS9htVoEf4F7BiZrfaBohzkuRu+NmtLnjAvZb/E4r/GHUA3OayGBN\ncGOOWlaepnJ9eN3m/65uudevSjHNIAqk+sLn5J8mDIVvuJP+/DrpVccAA60N+tiO\nq3XbHOCIblOUiIyKspGPMk2YUkLvytwTNpzaWkhwbOBuZERYtawv1YrC5pbDd/R/\n/5GvErK8UDlE6j6mJ+CLsuCB43Wyyo6a3eCP9JN6WuvVMNgxCLie5UQYH/a3puZ2\n2bZn3xLiXntP/rx02NpPNMDfQErDM/QIV3xubsH5xHXW3Ypv2O4MyVpdClABVT2t\n+Xx6H39HUOntS1leMa8cJk5tT+FYGYfUSOf01w+3BgxKHdww65DcNMX3MFJyKbQ5\nSt8lBt/Y8ODssy2IFUzkfAJzTYssBmiyg6FPUtw+tDa1Z4riJ6hlOkc3hCh7HXxu\n/oPLOwLUONfcrTMyMxkbl+KTSGdHAai/dyPlHZT/zXlnKaR8Q+XHBn5905e2HytH\ntccr7fuvjRlRDHvX/fQ9kBumBDTH13WKb45jEyARI1f6xUd7qdIQl+mePUNtkjrU\nYpOc5PKTY53wSFJX5PYueYVBQEpen+Rcv6ozWK0ooFh7hOHb0iyiJoWq7zZHTHO3\nSfNSPeCk/Y9BrEXe+JW6Eih7oL3VUO1TzJ7QpFvt5svT7IgaUuQF2TESA4x+own3\niU9E16D6raUtHYlqXjJtl8klYC+B0o/3LOISnVgeTZXb3wpBL4LIlGq1ZOlYqkrS\nKJY8tq1b1PbAQS1S8u4YOeNyyWIEJUJkk9VMakcEzTUj/pfnLqvi23zFd/sSexyt\n0VhgahhYcGwnJ4TJsRkK7Y3SVpngBjCpL9KH0xRTtY0g8ugUGpmdKsh67vxThI3V\nZNB9NYN8dxD80wqOYjvWlgO79hE2GTLGQp0wv2m5/1kVQYnkM/fBltghXam4IQmU\nJ6Higx6UIlSZ8J7eHO1oN+cI16o+GMoaIVxDJG9+u1iSdvC3VC0QP+ek700nGt6y\ncQ3wBbnuJiv6tZbjqV0ZMM1e2XhBvn31IKVrJu0ozguwdqcCM8XwhyS5mISuRB+4\niRSZB8eOUvORFBIm1NZD1fdcmmSSYvUxND6AOXZilETESW34GgQcS7Ft8zJ4uvdr\n/WLSNXYoDO5QywqrWc+G3Kw0whXYDBwkfjdGD/taI1q4hyyosPJ4HeRiNf/uV0Nc\nFH/McwlxZvX+Fianr5t1rrtNv7EICfWtcdC//agXXF2+gwutOIYp0l+ajL8GnPwc\nniqXvWO+zspEhEuXzIiAQfR30dZ9lUafUf1Iyy5/G145EPEUXl38uOY=\n-----END ENCRYPTED PRIVATE KEY-----\n",
        "privatekey_pass": "q"
    }
}
```

## Instructions
1. Use the SQLAlchemy URL above to connect to your Snowflake database
2. Use the Security JSON configuration for authentication
3. The private key is already formatted with escaped newlines for direct use
