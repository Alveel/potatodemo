FROM registry.access.redhat.com/ubi8/python-38

USER root

RUN yum install cairo cairo-gobject

USER 1001
