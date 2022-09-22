keys:
  result:
    value: "{{ bgp_peers }}"
    top: bgp-information/bgp-peer
    items:
      address: peer-address
      asn: peer-as
      state: peer-state
vars:
  bgp_peers:
    address: "{{ item.address }}"
    asn: "{{ item.asn }}"
    state: "{{ item.state }}"