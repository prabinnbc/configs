#!/usr/bin/env python

hostnames = ["csr1kv1", "csr1kv2", "csr1kv3"]

for hostname in hostnames:
        print(
                        "Performing configuration backup for host: {hostname}".format(
                                        hostname=hostname
                                                )
                            )
