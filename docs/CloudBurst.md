LDPC: logical disaggregation with physical colocation

- Function executor: 
	- retrives and deserialized the requested function
	- transpartently resolved all KVS reference function arguments in parallel
- cache
	- interact with executors via IPC
	- when receving update from executetor, it updates data locally, acknoledges the request, and asynchronously send the result to the KVS to be merged.
	- If data does not exist locally, it asynchronously retrives it from the KVS
	- Fressness
		- Each cache periodically publishes a snapshot of its cached keys to the KVS
		- Anna accept the keyset and construct an index that maps each key to the caches incrmentally. Anna propogate this index to periodically propogate key updates to caches.
- Function Schedulers:
	- Scheduling Mechanism
		- single function vs DAG(topology stores in Anna)
		- each schedule keep tracks index of keys stored by each cache
	- Scheduling Policy 
		- the scheduler inspects its local cached key
index and picks the executor with the most data cached locally—to
take advantage of locality, the user must specify KVS references
- Resource management SYstem