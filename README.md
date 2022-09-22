# DYI Intent-based Networking with Ansible

## steps:
### create intended topology in 'intent.yaml'
looks like:
```
---
spines:
  - name: R1
    mgmt_ip: 10.255.255.101

leaves:
  - name: R3
    mgmt_ip: 10.255.255.103
  - name: R4
    mgmt_ip: 10.255.255.104
```
### parse intent
`ansible-playbook -i localhost, pb_1_parse_intent.yaml`
### push config
`ansible-playbook -i inventory pb_2_push_intent.yaml`
### verify intent
`ansible-playbook -i inventory pb_3_verify_intent.yaml`