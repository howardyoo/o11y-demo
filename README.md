# example app

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

- Insight is costly

## DB

- Vendored Queue

- Insight possible, just never taken advantage of

## Diagram

![diagram](diagram.png "diagram")
