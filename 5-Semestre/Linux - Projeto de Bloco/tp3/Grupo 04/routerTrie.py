
from trieNode import TrieNode  

class RouterTrie:
    def __init__(self):
        self.root = TrieNode()

    def _ip_to_bits(self, ip: str):
        if ':' in ip: 
            expanded = ip.replace('::', ':0000:')
            groups = expanded.split(':')
            bits = []
            for group in groups:
                if group:
                    val = int(group, 16)
                    for i in range(15, -1, -1):
                        bits.append((val >> i) & 1)
            return bits
        else:  
            octets = [int(x) for x in ip.split('.')]
            bits = []
            for octet in octets:
                for i in range(7, -1, -1):
                    bits.append((octet >> i) & 1)
            return bits

    def insert(self, cidr: str, route_id: int):
        prefix, mask_str = cidr.split('/')
        mask_len = int(mask_str)
        
        bits = self._ip_to_bits(prefix)
        
        node = self.root
        for i in range(mask_len):
            bit = bits[i]
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        
        node.route_id = route_id
        node.is_terminal = True

    def lookup(self, ip: str) -> int:
        """Busca Longest Prefix Match (LPM)"""
        bits = self._ip_to_bits(ip)
        node = self.root
        best_route = None
        
        for bit in bits:
            if node.is_terminal:
                best_route = node.route_id
                
            if node.children[bit] is None:
                break
            node = node.children[bit]
        
        if node and node.is_terminal:
            best_route = node.route_id
            
        return best_route