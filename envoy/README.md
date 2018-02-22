# Envoy Check

## Overview



## Setup
### Installation

The envoy check is packaged with the Agent, so simply [install the Agent](https://app.datadoghq.com/account/settings#agent) anywhere you wish to use it.

If you need the newest version of the Envoy check, install the `dd-check-envoy` package; this package's check overrides the one packaged with the Agent. See the [integrations-core repository README.md for more details](https://github.com/DataDog/integrations-core#installing-the-integrations).

### Configuration

If you want to configure the check with custom options, create a file `envoy.yaml` in the Agent's `conf.d` directory. See the [sample envoy.yaml](https://github.com/DataDog/integrations-core/blob/master/envoy/conf.yaml.example) for all available configuration options.

### Validation

[Run the Agent's `status` subcommand](https://docs.datadoghq.com/agent/faq/agent-status-and-information/) and look for `envoy` under the Checks section:

```
  Checks
  ======
    [...]

    envoy
    -------
      - instance #0 [OK]
      - Collected 40 metrics, 0 events & 0 service checks

    [...]
```

## Data Collected
### Metrics

See [metadata.csv](https://github.com/DataDog/integrations-core/blob/master/envoy/metadata.csv) for a list of metrics provided by this integration.

### Events
The Envoy check does not include any event at this time.

### Service Checks
The Envoy check does not include any service check at this time.

## Troubleshooting
Need help? Contact [Datadog Support](http://docs.datadoghq.com/help/).

## Further Reading
Learn more about infrastructure monitoring and all our integrations on [our blog](https://www.datadoghq.com/blog/)
