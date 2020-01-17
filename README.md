# InfoGat

automate domain enumeration and information
gathering with domain default target midtrans.com

how to use :
$python3 goMerch.py

requirement :
- json
- requests
- date
- dnsdumpster

output json example :
```
superuser-2:infogat andranaradyka$ python3 goMerch.py 
list index out of range
{
  "waktu": "10:40:53",
  "tanggal": "2020-01-17",
  "data": [
    {
      "shodan": [
        {
          "host": "103.242.107.203",
          "port": 2083,
          "ssl chiper": "TLSv1/SSLv3"
        }
      ],
      "SecurityTrails": [
        {
          "hostname": "midtrans.com",
          "response": "104.17.134.16"
        },
        {
          "subdomain": [
            "account",
            "account-gopay",
            "admin",
            "aegis",
            "analytics",
            "andes",
            "api",
            "api-docs",
            "api.google",
            "api.sandbox",
            "api.sg",
            "api.stg",
            "app",
            "app.sandbox",
            "athena-docs",
            "blog",
            "cf-lb-api",
            "cf-lb-api-sg",
            "cf-lb-garuda",
            "cf-lb.api.google",
            "cf-lb.pvt00068",
            "cf-lb.sandbox",
            "checkout",
            "dashboard",
            "dashboard-gopay",
            "dashboard.sandbox",
            "dc1-pmm.ops",
            "dc1.ops",
            "dc11-graylog.ops",
            "demo",
            "demostore",
            "diesel.stg",
            "dimas.sandbox",
            "docs",
            "email.mg",
            "engineering",
            "fingerprint",
            "gencert.ops",
            "grafana.ops",
            "igs.sandbox",
            "internal.sandbox",
            "iris-banksim.sandbox",
            "iris-docs",
            "iris.sandbox",
            "jkt",
            "kafkamgr.sandbox",
            "mobile",
            "mobile-docs",
            "mrt.ops",
            "ops",
            "ops.sandbox",
            "passport",
            "passport-cb",
            "passport-cb.sandbox",
            "passport-gopay",
            "passport.sandbox",
            "payments",
            "rancher",
            "recurring",
            "sandbox",
            "simulator.sandbox",
            "snap-docs",
            "status",
            "stg",
            "stg-checkout",
            "store",
            "support",
            "unicorn.ops",
            "vt-pixels",
            "vtweb2",
            "www",
            "www.checkout"
          ]
        }
      ],
      "censys": [
        {
          "domain": "midtrans.com",
          "protocol": [
            "443/https_www",
            "443/https",
            "80/http_www",
            "25/smtp",
            "80/http"
          ]
        }
      ],
      "dnsdumpster": [
        {
          "domain": "midtrans.com",
          "subdomain": [
            {
              "subdomain": "vtweb2.midtrans.com",
              "ip address": "104.16.22.31"
            },
            {
              "subdomain": "cf-lb.pvt00068.midtrans.com",
              "ip address": "103.44.26.216"
            },
            {
              "subdomain": "cf-lb-garuda.midtrans.com",
              "ip address": "103.127.17.25"
            },
            {
              "subdomain": "dashboard.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "cf-lb.api.google.midtrans.com",
              "ip address": "103.208.23.37"
            },
            {
              "subdomain": "store.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "recurring.midtrans.com",
              "ip address": "103.44.27.121"
            },
            {
              "subdomain": "api.stg.midtrans.com",
              "ip address": "117.102.118.210"
            },
            {
              "subdomain": "api.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "demo.midtrans.com",
              "ip address": "104.17.133.16"
            },
            {
              "subdomain": "app.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "rancher.midtrans.com",
              "ip address": "103.58.100.231"
            },
            {
              "subdomain": "analytics.midtrans.com",
              "ip address": "103.58.101.207"
            },
            {
              "subdomain": "docs.midtrans.com",
              "ip address": "104.17.133.16"
            },
            {
              "subdomain": "mobile-docs.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "api-docs.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "snap-docs.midtrans.com",
              "ip address": "104.17.133.16"
            },
            {
              "subdomain": "andes.midtrans.com",
              "ip address": "103.58.100.231"
            },
            {
              "subdomain": "aegis.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "vt-pixels.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "ops.midtrans.com",
              "ip address": "103.208.23.22"
            },
            {
              "subdomain": "dc1.ops.midtrans.com",
              "ip address": "103.208.23.22"
            },
            {
              "subdomain": "grafana.ops.midtrans.com",
              "ip address": "103.44.26.169"
            },
            {
              "subdomain": "unicorn.ops.midtrans.com",
              "ip address": "103.44.26.169"
            },
            {
              "subdomain": "gencert.ops.midtrans.com",
              "ip address": "103.58.103.188"
            },
            {
              "subdomain": "payments.midtrans.com",
              "ip address": "103.208.23.14"
            },
            {
              "subdomain": "status.midtrans.com",
              "ip address": "104.17.133.16"
            },
            {
              "subdomain": "fingerprint.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "account.midtrans.com",
              "ip address": "104.16.44.37"
            },
            {
              "subdomain": "checkout.midtrans.com",
              "ip address": "128.199.202.169"
            },
            {
              "subdomain": "stg-checkout.midtrans.com",
              "ip address": "128.199.117.104"
            },
            {
              "subdomain": "www.midtrans.com",
              "ip address": "104.17.133.16"
            },
            {
              "subdomain": "cf-lb.sandbox.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "api.sandbox.midtrans.com",
              "ip address": "103.58.103.188"
            },
            {
              "subdomain": "app.sandbox.midtrans.com",
              "ip address": "103.58.103.188"
            },
            {
              "subdomain": "dimas.sandbox.midtrans.com",
              "ip address": "103.44.26.169"
            },
            {
              "subdomain": "igs.sandbox.midtrans.com",
              "ip address": "103.58.103.188"
            },
            {
              "subdomain": "dashboard-gopay.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "account-gopay.midtrans.com",
              "ip address": "104.17.2.81"
            },
            {
              "subdomain": "passport-gopay.midtrans.com",
              "ip address": "104.17.2.81"
            }
          ]
        }
      ]
    }
  ]
}

```
