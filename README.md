# AWX (Ansible tower distribution) on Docker

<p align="center">
<img src="./docs/img/AWX login.PNG" width="80%">
</p>

Run the latest version of [AWX][awx-github] with Docker and Docker Compose.

AWX provides a web-based user interface, [REST API](https://docs.ansible.com/ansible-tower/latest/html/towerapi/api_ref.html), and task engine built on top of [Ansible](https://github.com/ansible/ansible). It is the upstream project for [Tower](https://www.ansible.com/products/tower), a commercial derivative of AWX.


> :information_source: The stack include an [Elasticsearch beat](https://www.elastic.co/es/beats) image, [Metricbeat](https://www.elastic.co/es/beats/metricbeat) to send information to a [Elastic Stack](https://www.elastic.co/es/products/) about the status of the machine and services in the stack.
>
> Check out to the [Docker Elastic stack](https://github.com/AlanPadi95/docker-elastic-stack) development.

Based on the official Docker images from Ansible, Redis and PostgreSQL:

* [ansible/awx](https://hub.docker.com/r/ansible/awx)
* [redis](https://hub.docker.com/_/redis/)
* [postgres](https://hub.docker.com/_/postgres)

Addtitional images:
* [store/elastic/metricbeat](https://hub.docker.com/_/metricbeat)

## Requirements
### Host setup

* [Docker Engine](https://docs.docker.com/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* 1.5 GB of RAM

By default, the stack exposes the following ports:

* 80: AWX web page

### Docker for Desktop

#### Windows

Ensure the [Shared Drives][win-shareddrives] feature is enabled for the `C:` drive.

#### MacOS

The default Docker for Mac configuration allows mounting files from `/Users/`, `/Volumes/`, `/private/`, and `/tmp`
exclusively. Make sure the repository is cloned in one of those locations or follow the instructions from the
[documentation][mac-mounts] to add more locations.

## Usage

### Bringing up the stack

Clone this repository, then start the stack using Docker Compose:

```console
$ git clone https://github.com/AlanPadi95/docker-awx-stack.git
...
$ docker-compose up
```

You can also run all services in the background (detached mode) by adding the `-d` flag to the above command.

> :information_source: You must run `docker-compose build` first whenever you switch branch or update a base image.

If you are starting the stack for the very first time, please read the section below attentively.

### Cleanup

AWX data is persisted in PostgreSQL server, inside a volume by default.

In order to entirely shutdown the stack and remove all persisted data, use the following Docker Compose command:

```console
$ docker-compose down -v
```

### Swarm mode

Support for Docker [Swarm mode][swarm-mode] is provided in the form of a `docker-compose.yml` file, which can
be deployed in an existing Swarm cluster using the following command:

```console
$ docker stack deploy -c docker-compose.yml awx
```

If all components get deployed without any error, the following command will show 6 running services:

```console
$ docker stack services awx
```

## Configuration

### User authentication

The stack is pre-configured with the following **privileged** user:

* user: *admin*
* password: *password*

For more information about AWX configurations, please take a little look to the official [administration guide][tower-admin-guide], the [user guide][tower-user-guide] and the [official GitHub Repository][awx-github].

[tower-admin-guide]: https://docs.ansible.com/ansible-tower/latest/html/administration/index.html

[tower-user-guide]: https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html

[awx-github]: https://github.com/ansible/awx

[swarm-mode]: https://docs.docker.com/engine/swarm/

[win-shareddrives]: https://docs.docker.com/docker-for-windows/#shared-drives

[mac-mounts]: https://docs.docker.com/docker-for-mac/osxfs/
