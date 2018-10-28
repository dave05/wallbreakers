class Solution:
    def subdomainVisits(self, cpdomains):
        visit_counter=collections.defaultdict(int)
        for d_visit in cpdomains:
            visits=int(d_visit.split(' ')[0])
            domain=d_visit.split(' ')[1]

            domain_list=domain.split('.')
            sub_domain=''
            for i in range(len(domain_list)-1,-1,-1):
                if sub_domain:
                    sub_domain=domain_list[i]+"."+sub_domain
                else:
                    sub_domain=domain_list[i]
                visit_counter[sub_domain]+=visits
        output=[]
        for key, value in visit_counter.items():
            visit=str(value)+" "+str(key)
            output.append(visit)
        return output


        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
