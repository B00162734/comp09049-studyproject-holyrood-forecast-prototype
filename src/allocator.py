"""
SeatAllocator
--------------
"""

class SeatAllocator(object):
    def allocate_dhondt(self,forecast, seats_available: int):
        seats_won_so_far = {'SNP':0, 'Con':0, 'Lab':0, 'Green':0, 'Lib Dem':0, 'Alba':0, 'UKIP':0, 'Ref UK':0, 'SSP':0 }

        for seats in range(seats_available):
            #   for q=v/s+1 where q is the quotient (projected number of total seats won)
            #   v is the number of votes received or in our case the forecasted number of seats per   party
            #   s is the number of seats won so far
            
            q = {party:forecast[party] / (seats_won_so_far[party] + 1) for party in forecast}
            max_key = max(q, key = q.get)
            seats_won_so_far[max_key] += 1
        return seats_won_so_far