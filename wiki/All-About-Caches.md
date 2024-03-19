## All About Caches

### Caching Overview

# Cache Performance Formula
_**(Average MemoryAccessTime) = (HitTime) * (Miss Penalty)**_

# Block Placement
A key cache design design is where blocks/lines are allowed to be placed within a cache. 

1. Set Associative --> A "set" is a group of blocks in the cache, the block is first mapped into a set and					   	   then can be placed anywhere within the set. If there are N sets the cache is said to  					    be N-Way set associative
2. 

# Types of Cache Misses
- Compulsory --> first access to a block will not be in cache, AKA cold cache, cold start misses
- Capacity --> if cache size cannot hold the program working set size blocks will be evicted and later 		 				retrieved
- Conflict --> if the block placement strategy is not fully associative, blocks that map to the same 					   location will evict each other

# Cache Optimization Targets
1. Reduce Hit Time
2. Increase Cache Bandwitdth
3. Reduce Miss Penalty
4. Reduce Miss Rate
5. Increase Parallelism

See: Cache Optimizations



