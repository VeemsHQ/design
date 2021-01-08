# Infrastructure Design

## K8s

### Intro

App comprises of a few containers:

1. webapp (serves HTTP calls)
2. celery-worker-general (processes misc background tasks, e.g. writing things to the DB, Downloading data, Uploading data)
3. celery-worker-media (processed media related background tasks, e.g. video transcoding. Very computationally expensive things.)
4. celery-worker-beat (celery 'beat' worker, schedules tasks to other worker types above)


### Deployment

All in 1 Cluster initially, in US east coast datacenter.

Comprises of 4 Deployments and 4 Pods with names:

- webapp
- celery-worker-beat
- celery-worker-general
- celery-worker-media


Comprises of one Service, which exposes `webapp` to the outside world.


Example (Number of Nodes and Pods below are variable based on config/load):

```

Node 1 (label=low-cpu)
----------------------------------------------------------------
|                                                              |
|        Deployment+POD webapp                                 |
|        -----------------------------------------------       |
|        |            (webapp container)                |      |
|        -----------------------------------------------       |
|                                                              |
|        Deployment+POD celery-worker-beat                     |
|        -----------------------------------------------       |
|        |        (webapp celery-worker-beat)           |      |
|        -----------------------------------------------       |
|                                                              |
|        Deployment+POD celery-worker-general                  |
|        -----------------------------------------------       |
|        |      (webapp celery-worker-general)          |      |
|        -----------------------------------------------       |
|                                                              |
----------------------------------------------------------------

Node 2 (label=low-cpu)
----------------------------------------------------------------
|                                                              |
|        Deployment+POD webapp                                 |
|        -----------------------------------------------       |
|        |            (webapp container)                |      |
|        -----------------------------------------------       |
|                                                              |
|        Deployment+POD celery-worker-beat                     |
|        -----------------------------------------------       |
|        |        (webapp celery-worker-beat)           |      |
|        -----------------------------------------------       |
|                                                              |
|        Deployment+POD celery-worker-general                  |
|        -----------------------------------------------       |
|        |      (webapp celery-worker-general)          |      |
|        -----------------------------------------------       |
|                                                              |
----------------------------------------------------------------

Node 3 (label=high-cpu)
----------------------------------------------------------------
|                                                              |
|        Deployment+POD celery-worker-media                    |
|        -----------------------------------------------       |
|        |      (webapp celery-worker-media)            |      |
|        -----------------------------------------------       |
|                                                              |
|                                                              |
|        Deployment+POD celery-worker-media                    |
|        -----------------------------------------------       |
|        |      (webapp celery-worker-media)            |      |
|        -----------------------------------------------       |
|                                                              |
----------------------------------------------------------------

Node 4 (label=high-cpu)
----------------------------------------------------------------
|                                                              |
|        Deployment+POD celery-worker-media                    |
|        -----------------------------------------------       |
|        |      (webapp celery-worker-media)            |      |
|        -----------------------------------------------       |
|                                                              |
----------------------------------------------------------------


... etc (I assume many Pods may be places in one or more Nodes as available)

```
