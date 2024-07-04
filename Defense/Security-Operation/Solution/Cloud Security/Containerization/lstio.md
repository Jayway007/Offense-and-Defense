## Definition
Istio is a service mesh—a modernized service networking layer that provides a transparent and language-independent way to flexibly and easily automate application network functions. It is a popular solution for managing the different microservices that make up a cloud-native application. 

## Relationships
- Envoy

Service meshes like Istio are made up of both a control plane and a data plane. Istio uses an extended version of Envoy as its data plane. Envoy then manages all inbound and outbound traffic in the Istio service mesh. 

- Kubernetes

Kubernetes, on the other hand, is an open source platform that gets rid of many of the manual processes involved in deploying and scaling containerized applications by automating and orchestrating them. And, although Istio is platform independent, using Istio and Kubernetes together is popular among developers.
