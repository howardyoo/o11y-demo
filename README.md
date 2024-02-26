# example app

## Diagram

![diagram](diagram.png "diagram")

## WAF

- Vendored WAF

- Not much insight

- Limited API

## Web

- Mix of NGINX and Apache

## Tier 1

- 95% Java apps

- All T1s cannot read/write from data tier

- Many will write event to queue, or comm with SaaS
  - "A user is attempting to log in"

## Tier 2

- 95% Java apps

- Only tier that can access data we store

- Critical

## DB

- Vendored DB

- Insight is costly, so limit use

## Queue

- Vendored Queue

- Insight possible, just never taken advantage of

## SaaS

- Vendored SaaS (honestly, could be some other internal team with an API)

- Insight not possible, or very limited

# Questions

## ENRICHMENT

- how do we enrich services we own ??
  - e.g. java app

- how do we enrich services we do NOT own, but have access to underlying APIs ??
  - e.g. RDS

- how do we enrich services we do NOT own AND have a limited API ??
  - e.g. imperva WAF

## SERVER MONITORING

- is this a tool that would be a replacement for traditional server monitoring ??
  - e.g. nagios // USE stats

- IF so, how would that be done ??

## ALERTING

- is there alerting ??

- how is alerting managed ??

- what delivery options are there ??
  - e.g. email, slack, SMS

## REPORTING

- personal dashboards ??

- shareable, community dashboards ??

- shareable, team only dashboards ??

- CRON report generation and delivery options
  - e.g. send PDF, via email, once a week to XYZ ??

## RBAC

- is there SSO capabilities ??

- what controls does one have over access to the various components ??

- how are keys created/issued/expired ??

## INFO

- 300+ mil events ingested everyday

- 230+ mil PROD events ingested everyday
