# Savings-heuristic algorithm for Travelling-salesman problem

First, all the nodes are sorted in ascending order of total edge-costs from each node. (sum of all column-values in a row of the cost-matrix.)

Then, the savings-heuristic algorithm is run iteratively, using different nodes as the starting-node.

The lowest tour-cost valid-tour generated from all the iterations, is found.

The iterations start, using the sorted nodes-list for starting-node, but also sometimes use randomly-selected starting-nodes to introduce an element of exploration in the search-algorithm.

The same savings-heuristic algoritm works for both euclidean and non-euclidean travelling-salesman problems.

## Test-run results for the 8 test-cases given for travelling-salesman problem.

| Test-cases | 0, euc_10 | 1, non-euc_10 | 2, euc_25 | 3, non-euc_25| 4, euc_50 | 5, non-euc_50| 6, euc_100 | 7, non-euc_100 |
|--|--|--|--|--|--|--|--|--|
| 24-8-2026 | 655.6751331590185 | 768.988361117 | 964.812249689 | 1609.268829199 | 1340.460459118 | 3109.62367178 | 1814.262870419 | 5688.3586401872 |
| 26-8-2026 11:47 | 655.6751331590184, (7) | 754.71076386199, (1) | 919.082356725, (17) | 1726.442756836, (17) | 1319.92637077, (17) | 3147.410918719, (6) | 1791.15178762, (85) | 5746.500427348, (69) |
| 26-8-2026 11:52 | 655.6751331590184, (5) | 693.48129862649, (2) | 845.0878576714, (11) | 1576.720440208, (9) | 1223.4319945288, (48) | 2934.84797799, (8) | 1699.094389369, (88) | 5688.3586401872, (20) |
| 26-8-2026 11:53 | 655.6751331590184, (5) | 673.7787665244, (9) | 845.0878576714, (11) | 1584.7737918, (4) | 1241.6814249, (20) | 2995.65760728, (33) | 1736.687648228, (34) | 5635.42056207, (0) |
| 26-8-2026 11:54 | 655.6751331590184, (5) | 673.7787665244, (9) | 787.5752663189, (24) | 1576.720440208, (9) | 1223.4572162, (29) | 2934.84797799, (8) | 1707.964491164, (59) | 5591.8855703, (3) |
| 26-8-2026 12:16 | 655.6751331590184, (5) | 673.7787665244, (9) | 787.5752663189, (24) | 1576.720440208, (9) | 1196.460993216, (26) | 2934.84797799, (8) | 1693.69099236, (22) | 5622.59455523, (81) |
| 26-8-2026 12:17 | 655.6751331590184, (5) | 673.7787665244, (9) | 787.5752663189, (24) | 1576.720440208, (9) | 1196.460993216, (26) | 2934.84797799, (8) | 1686.784307951, (99) | 5591.8855703, (3) |
