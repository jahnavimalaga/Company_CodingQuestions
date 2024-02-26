from sample import Queue
"""
This is funtion is to find the completion times of each member who comes to the counter
it is said that if the queue is more than 10 then the new person who comes to purchase something
at the counter will leave, otherwise they join the queue. The processing time at the counter is 300 sec
and the leaving person's completion time would be same as its arrival time
"""
def solution(times):

    completion_times = []
    next_starting_time = 0 

    my_queue = Queue()

    for arrival_time in times:
        if arrival_time>=next_starting_time:
            next_starting_time = max(next_starting_time,arrival_time)
            completion_time = next_starting_time+300
            next_starting_time = completion_time
            completion_times.append(completion_time)
        else:
            can_insert = False
            # queue is empty
            if my_queue.is_empty():
                can_insert = True
            # queue is not full
            elif len(my_queue.queue) < 11:
                can_insert = True

            # queue is full, so we check if we can empty something
            else:
                for member_ct in my_queue.queue[:]:
                    if member_ct<arrival_time:
                        my_queue.dequeue()
                        can_insert = True
                        continue
                    else:
                        break
            if can_insert:
                    next_starting_time = max(next_starting_time,arrival_time)
                    completion_time = next_starting_time+300
                    next_starting_time = completion_time
                    my_queue.enqueue(completion_time)
                    completion_times.append(completion_time)
            else:                
                completion_time = arrival_time
                completion_times.append(completion_time)
    
    print("queue:",my_queue.queue)
            
    return completion_times

if __name__ == "__main__":
    times = [i for i in range(1,15)]+ [602]
    output = solution(times)
    print("output:",output)