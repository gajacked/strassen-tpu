> INTERIM SNAPSHOT: 113/168 shapes; the experiment is still running.

# Joint MM tuning results and decisions

168 development geometries, separate FP32 and BF16 output. BF16 inputs/pre-adds; FP32 accumulation/reconstruction; final output store included in time and error.
Screening ranks each candidate against the repeated Native_default anchor in its compilation batch. Choices are frozen before three fresh inputs × 30 paired confirmation rounds.
Recommendations retain the frozen overall winner only if all error checks pass, mean speedup over tuned Native is at least 1.01, and the pointwise paired 95% interval lies above 1. Otherwise they fall back to the frozen tuned Native; they never promote another confirmation finalist.
All intervals are conditional on screening, with no multiple-comparison adjustment. Shapes and Gaussian input family are development data; numerical eligibility is not an arbitrary-input or model-quality guarantee.

## float32 output

| M × K × N | Recommended configuration | Native ms | Recommended ms | Speedup vs Native | Relative L2 % | Decision |
|---|---|---:|---:|---:|---:|---|
| 1 × 1 × 1 | Native | 0.2283 | 0.2283 | 1.0000 | 0.0000 | native_won_screening |
| 3 × 3 × 3 | Native | 0.2416 | 0.2416 | 1.0000 | 0.0000 | native_won_screening |
| 16 × 16 × 16 | Native | 0.2197 | 0.2197 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 64 × 64 × 64 | Native | 0.2203 | 0.2203 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 128 × 128 × 128 | Native | 0.2284 | 0.2284 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 256 × 256 | Native | 0.2191 | 0.2191 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 8 × 2048 × 2048 | Native | 0.2253 | 0.2253 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 8 × 2048 | Native | 0.2267 | 0.2267 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 2048 × 8 | Native | 0.2290 | 0.2290 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 384 × 384 × 384 | Native | 0.2286 | 0.2286 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 384 × 1024 × 256 | Native | 0.2417 | 0.2417 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 512 × 512 | Native | 0.2397 | 0.2397 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 1024 × 768 | Native | 0.2590 | 0.2590 | 1.0000 | 0.0000 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 512 × 512 × 768 | Native | 0.2265 | 0.2265 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 384 × 1536 × 512 | Native | 0.2245 | 0.2245 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 2048 × 384 | Native | 0.2459 | 0.2459 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 3072 × 256 | Native | 0.2376 | 0.2376 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 768 × 768 × 768 | Native | 0.2415 | 0.2415 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 6144 × 256 | Native | 0.2260 | 0.2260 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 1536 × 2048 × 256 | Native | 0.2398 | 0.2398 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 1023 × 1023 × 1023 | Native | 0.2368 | 0.2368 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 64 × 512 × 32768 | Native | 0.2558 | 0.2558 | 1.0000 | 0.0000 | native_won_screening |
| 256 × 2048 × 2048 | Native | 0.2273 | 0.2273 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 1024 × 1024 × 1024 | Native | 0.2377 | 0.2377 | 1.0000 | 0.0000 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 2048 × 256 × 2048 | Native | 0.2344 | 0.2344 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 2048 × 256 | Native | 0.2411 | 0.2411 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 32768 × 512 × 64 | Native | 0.2426 | 0.2426 | 1.0000 | 0.0000 | native_won_screening |
| 1025 × 1025 × 1025 | Native | 0.2389 | 0.2389 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 6144 × 768 | Native | 0.2510 | 0.2510 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 1024 × 768 | Native | 0.2367 | 0.2367 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 384 × 3072 × 2048 | Native | 0.2551 | 0.2551 | 1.0000 | 0.0000 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 384 × 16384 × 384 | Native | 0.2526 | 0.2526 | 1.0000 | 0.0000 | native_won_screening |
| 256 × 2048 × 6144 | Native | 0.2347 | 0.2347 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4096 × 1536 × 512 | Native | 0.2355 | 0.2355 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 32768 × 256 × 384 | Native | 0.2817 | 0.2817 | 1.0000 | 0.0000 | native_won_screening |
| 384 × 1536 × 12288 | Native | 0.2752 | 0.2752 | 1.0000 | 0.0000 | native_won_screening |
| 2048 × 2048 × 2048 | Native | 0.2680 | 0.2680 | 1.0000 | 0.0000 | native_won_screening |
| 256 × 1536 × 24576 | Native | 0.3114 | 0.3114 | 1.0000 | 0.0000 | native_won_screening |
| 384 × 6144 × 4096 | Cubic [512, 512, 6144] | 0.2966 | 0.2801 | 1.0588 | 0.0000 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 256 × 16384 × 4096 | Native | 0.3305 | 0.3305 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4096 × 256 × 16384 | Native | 0.4088 | 0.4088 | 1.0000 | 0.0000 | native_won_screening |
| 16384 × 256 × 4096 | Native | 0.4061 | 0.4061 | 1.0000 | 0.0000 | native_won_screening |
| 256 × 24576 × 3072 | Native | 0.3505 | 0.3505 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 49152 × 1536 | Native | 0.3466 | 0.3466 | 1.0000 | 0.0000 | native_won_screening |
| 384 × 384 × 131072 | Native | 0.4479 | 0.4479 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 8192 × 1536 | Native | 0.3038 | 0.3038 | 1.0000 | 0.0000 | native_won_screening |
| 6144 × 2048 × 1536 | Native | 0.2855 | 0.2855 | 1.0000 | 0.0000 | native_won_screening |
| 768 × 3072 × 12288 | Native | 0.3864 | 0.3864 | 1.0000 | 0.0000 | native_won_screening |
| 768 × 12288 × 3072 | Native | 0.3444 | 0.3444 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 3072 × 768 × 12288 | Native | 0.5040 | 0.5040 | 1.0000 | 0.0000 | native_won_screening |
| 3072 × 12288 × 768 | Native | 0.3634 | 0.3634 | 1.0000 | 0.0000 | native_won_screening |
| 12288 × 768 × 3072 | Native | 0.3349 | 0.3349 | 1.0000 | 0.0000 | native_won_screening |
| 12288 × 3072 × 768 | Native | 0.3458 | 0.3458 | 1.0000 | 0.0000 | native_won_screening |
| 2047 × 4096 × 4096 | Native | 0.3517 | 0.3517 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 8191 × 2048 | Native | 0.3370 | 0.3370 | 1.0000 | 0.0000 | native_won_screening |
| 512 × 4096 × 16384 | Native | 0.3531 | 0.3531 | 1.0000 | 0.0000 | native_won_screening |
| 512 × 16384 × 4096 | Native | 0.3554 | 0.3554 | 1.0000 | 0.0000 | native_won_screening |
| 2048 × 1024 × 16384 | Native | 0.3719 | 0.3719 | 1.0000 | 0.0000 | native_won_screening |
| 4096 × 512 × 16384 | Native | 0.4148 | 0.4148 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4096 × 16384 × 512 | Native | 0.3474 | 0.3474 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 16384 × 512 × 4096 | Native | 0.4344 | 0.4344 | 1.0000 | 0.0000 | native_won_screening |
| 16384 × 4096 × 512 | Native | 0.3590 | 0.3590 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 8193 × 2048 | Native | 0.3540 | 0.3540 | 1.0000 | 0.0000 | native_won_screening |
| 2049 × 4096 × 4096 | Native | 0.3664 | 0.3664 | 1.0000 | 0.0000 | native_won_screening |
| 768 × 8192 × 6144 | Native | 0.3448 | 0.3448 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 384 × 65536 | Native | 0.5262 | 0.5262 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 16384 × 1536 | Native | 0.3742 | 0.3742 | 1.0000 | 0.0000 | native_won_screening |
| 12288 × 1536 × 2048 | Native | 0.3661 | 0.3661 | 1.0000 | 0.0000 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 32768 × 1024 × 1536 | Native | 0.4250 | 0.4250 | 1.0000 | 0.0000 | native_won_screening |
| 49152 × 512 × 2048 | Native | 0.5367 | 0.5367 | 1.0000 | 0.0000 | native_won_screening |
| 49152 × 4096 × 256 | Native | 0.5439 | 0.5439 | 1.0000 | 0.0000 | native_won_screening |
| 98304 × 1024 × 512 | Native | 0.5119 | 0.5119 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4095 × 4095 × 4095 | Native | 0.4322 | 0.4322 | 1.0000 | 0.0000 | native_won_screening |
| 2048 × 4096 × 8191 | Native | 0.4243 | 0.4243 | 1.0000 | 0.0000 | native_won_screening |
| 2048 × 2048 × 16384 | Native | 0.4221 | 0.4221 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 16384 × 2048 | Native | 0.4389 | 0.4389 | 1.0000 | 0.0000 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 4096 × 4096 × 4096 | Native | 0.4281 | 0.4281 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 16384 × 2048 × 2048 | S1 products; [1024, 2048, 2048]; b2 | 0.4475 | 0.4063 | 1.1013 | 0.4487 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 2048 × 4096 × 8193 | Native | 0.4422 | 0.4422 | 1.0000 | 0.0000 | native_won_screening |
| 4097 × 4097 × 4097 | Native | 0.4579 | 0.4579 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 32768 × 1536 | Native | 0.4356 | 0.4356 | 1.0000 | 0.0000 | native_won_screening |
| 3072 × 8192 × 3072 | Native | 0.4648 | 0.4648 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4608 × 4608 × 4608 | Native | 0.5108 | 0.5108 | 1.0000 | 0.0000 | native_won_screening |
| 256 × 98304 × 4096 | Native | 0.8062 | 0.8062 | 1.0000 | 0.0000 | native_won_screening |
| 512 × 16384 × 12288 | Native | 0.5547 | 0.5547 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 16384 × 1024 × 6144 | Native | 0.5461 | 0.5461 | 1.0000 | 0.0000 | native_won_screening |
| 65536 × 256 × 6144 | Native | 1.2979 | 1.2979 | 1.0000 | 0.0000 | native_won_screening |
| 768 × 24576 × 6144 | Native | 0.5568 | 0.5568 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 5120 × 5120 × 5120 | S1 products; [1024, 512, 5120]; b2 | 0.5945 | 0.5728 | 1.0379 | 0.4373 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 256 × 32768 × 16384 | Native | 0.9526 | 0.9526 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 2048 × 32768 | Native | 0.5716 | 0.5716 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 32768 × 2048 | S1 products; [2048, 2048, 1024]; b2 | 0.5770 | 0.5447 | 1.0593 | 0.4383 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 32768 × 2048 × 2048 | S1 products; [2048, 2048, 2048]; b2 | 0.5773 | 0.5619 | 1.0274 | 0.4439 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 131072 × 1024 × 1024 | Native | 0.8039 | 0.8039 | 1.0000 | 0.0000 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 1536 × 24576 × 4096 | Native | 0.6532 | 0.6532 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 65536 × 1536 | Native | 0.6274 | 0.6274 | 1.0000 | 0.0000 | native_won_screening |
| 3072 × 16384 × 3072 | Native | 0.6296 | 0.6296 | 1.0000 | 0.0000 | native_won_screening |
| 2048 × 32768 × 3072 | S1 products; [2048, 1024, 1024]; b2 | 0.7408 | 0.7243 | 1.0228 | 0.4485 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 3072 × 32768 × 2048 | Native | 0.7416 | 0.7416 | 1.0000 | 0.0000 | native_won_screening |
| 4096 × 2048 × 24576 | S1 products; [2048, 2048, 2048]; b2 | 0.7536 | 0.7236 | 1.0414 | 0.4427 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 4096 × 131072 × 384 | Native | 1.0184 | 1.0184 | 1.0000 | 0.0000 | native_won_screening |
| 768 × 49152 × 6144 | Native | 0.8077 | 0.8077 | 1.0000 | 0.0000 | native_won_screening |
| 2048 × 2048 × 65536 | S1 products; [2048, 2048, 2048]; b2 | 0.8981 | 0.8535 | 1.0522 | 0.4391 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 2048 × 65536 × 2048 | S1 products; [2048, 2048, 1024]; b2 | 0.8846 | 0.8300 | 1.0658 | 0.4440 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 4096 × 8192 × 8192 | S1 outputs; [1024, 512, 8192]; b2 | 0.9624 | 0.8881 | 1.0836 | 0.4387 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 4096 × 16384 × 4096 | S1 products; [2048, 2048, 1024]; b2 | 0.9186 | 0.8779 | 1.0463 | 0.4425 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 8192 × 4096 × 8192 | S1 outputs; [2048, 2048, 4096]; b2 | 0.9383 | 0.8738 | 1.0738 | 0.4418 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 8192 × 8192 × 4096 | S1 outputs; [2048, 2048, 4096]; b2 | 0.9366 | 0.8916 | 1.0505 | 0.4443 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 65536 × 2048 × 2048 | Native | 0.9007 | 0.9007 | 1.0000 | 0.0000 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 384 × 12288 × 65536 | Native | 1.3623 | 1.3623 | 1.0000 | 0.0000 | native_won_screening |
| 384 × 65536 × 12288 | Native | 1.3628 | 1.3628 | 1.0000 | 0.0000 | native_won_screening |
| 1536 × 131072 × 1536 | Native | 0.9945 | 0.9945 | 1.0000 | 0.0000 | native_won_screening |
| 8192 × 8192 × 8192 | S1 outputs; [2048, 2048, 4096]; b2 | 1.5925 | 1.4867 | 1.0712 | 0.4439 | frozen_winner_passed_errors_and_confirmed_speed_margin |

## bfloat16 output

| M × K × N | Recommended configuration | Native ms | Recommended ms | Speedup vs Native | Relative L2 % | Decision |
|---|---|---:|---:|---:|---:|---|
| 1 × 1 × 1 | Native | 0.2448 | 0.2448 | 1.0000 | 0.2787 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 3 × 3 × 3 | Native | 0.2481 | 0.2481 | 1.0000 | 0.1972 | native_won_screening |
| 16 × 16 × 16 | Native | 0.2433 | 0.2433 | 1.0000 | 0.1658 | native_won_screening |
| 64 × 64 × 64 | Native | 0.2205 | 0.2205 | 1.0000 | 0.1665 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 128 × 128 × 128 | Native | 0.2387 | 0.2387 | 1.0000 | 0.1678 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 256 × 256 | Native | 0.2237 | 0.2237 | 1.0000 | 0.1664 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 8 × 2048 × 2048 | Native | 0.2333 | 0.2333 | 1.0000 | 0.1670 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 8 × 2048 | Native | 0.2517 | 0.2517 | 1.0000 | 0.1695 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 2048 × 2048 × 8 | Native | 0.2308 | 0.2308 | 1.0000 | 0.1685 | native_won_screening |
| 384 × 384 × 384 | Native | 0.2455 | 0.2455 | 1.0000 | 0.1668 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 384 × 1024 × 256 | Native | 0.2341 | 0.2341 | 1.0000 | 0.1668 | native_won_screening |
| 512 × 512 × 512 | Native | 0.2469 | 0.2469 | 1.0000 | 0.1663 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 1024 × 768 | Native | 0.2547 | 0.2547 | 1.0000 | 0.1665 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 512 × 512 × 768 | Native | 0.2394 | 0.2394 | 1.0000 | 0.1664 | native_won_screening |
| 384 × 1536 × 512 | Native | 0.2342 | 0.2342 | 1.0000 | 0.1659 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 2048 × 384 | Native | 0.2411 | 0.2411 | 1.0000 | 0.1670 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 3072 × 256 | Native | 0.2389 | 0.2389 | 1.0000 | 0.1668 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 768 × 768 × 768 | Native | 0.2450 | 0.2450 | 1.0000 | 0.1662 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 512 × 6144 × 256 | Native | 0.2171 | 0.2171 | 1.0000 | 0.1666 | native_won_screening |
| 1536 × 2048 × 256 | Native | 0.2410 | 0.2410 | 1.0000 | 0.1663 | native_won_screening |
| 1023 × 1023 × 1023 | Native | 0.2479 | 0.2479 | 1.0000 | 0.1662 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 64 × 512 × 32768 | Native | 0.2619 | 0.2619 | 1.0000 | 0.1680 | native_won_screening |
| 256 × 2048 × 2048 | Native | 0.2328 | 0.2328 | 1.0000 | 0.1664 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 1024 × 1024 × 1024 | Native | 0.2358 | 0.2358 | 1.0000 | 0.1662 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 256 × 2048 | Native | 0.2400 | 0.2400 | 1.0000 | 0.1670 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 2048 × 256 | Native | 0.2384 | 0.2384 | 1.0000 | 0.1661 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 32768 × 512 × 64 | Native | 0.2616 | 0.2616 | 1.0000 | 0.1682 | native_won_screening |
| 1025 × 1025 × 1025 | Native | 0.2342 | 0.2342 | 1.0000 | 0.1680 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 256 × 6144 × 768 | Native | 0.2398 | 0.2398 | 1.0000 | 0.1664 | native_won_screening |
| 1536 × 1024 × 768 | Native | 0.2365 | 0.2365 | 1.0000 | 0.1670 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 384 × 3072 × 2048 | Native | 0.2530 | 0.2530 | 1.0000 | 0.1667 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 384 × 16384 × 384 | Native | 0.2547 | 0.2547 | 1.0000 | 0.1686 | native_won_screening |
| 256 × 2048 × 6144 | Native | 0.2413 | 0.2413 | 1.0000 | 0.1654 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4096 × 1536 × 512 | S1 products; [1024, 512, 1536]; b2 | 0.2485 | 0.2407 | 1.0323 | 0.4729 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 32768 × 256 × 384 | Native | 0.2609 | 0.2609 | 1.0000 | 0.1662 | native_won_screening |
| 384 × 1536 × 12288 | Native | 0.2668 | 0.2668 | 1.0000 | 0.1665 | native_won_screening |
| 2048 × 2048 × 2048 | Native | 0.2525 | 0.2525 | 1.0000 | 0.1677 | native_won_screening |
| 256 × 1536 × 24576 | Native | 0.3032 | 0.3032 | 1.0000 | 0.1666 | native_won_screening |
| 384 × 6144 × 4096 | S1 outputs; [512, 512, 3072]; b2 | 0.2953 | 0.2872 | 1.0284 | 0.4389 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 256 × 16384 × 4096 | Native | 0.3297 | 0.3297 | 1.0000 | 0.1659 | native_won_screening |
| 4096 × 256 × 16384 | Native | 0.3331 | 0.3331 | 1.0000 | 0.1666 | native_won_screening |
| 16384 × 256 × 4096 | Native | 0.3194 | 0.3194 | 1.0000 | 0.1678 | native_won_screening |
| 256 × 24576 × 3072 | Native | 0.3327 | 0.3327 | 1.0000 | 0.1678 | native_won_screening |
| 256 × 49152 × 1536 | Native | 0.3458 | 0.3458 | 1.0000 | 0.1688 | native_won_screening |
| 384 × 384 × 131072 | Native | 0.3731 | 0.3731 | 1.0000 | 0.1665 | native_won_screening |
| 1536 × 8192 × 1536 | Native | 0.2956 | 0.2956 | 1.0000 | 0.1669 | native_won_screening |
| 6144 × 2048 × 1536 | Native | 0.2930 | 0.2930 | 1.0000 | 0.1682 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 768 × 3072 × 12288 | Native | 0.3122 | 0.3122 | 1.0000 | 0.1662 | native_won_screening |
| 768 × 12288 × 3072 | Native | 0.3430 | 0.3430 | 1.0000 | 0.1662 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 3072 × 768 × 12288 | Native | 0.3519 | 0.3519 | 1.0000 | 0.1671 | native_won_screening |
| 3072 × 12288 × 768 | Native | 0.3647 | 0.3647 | 1.0000 | 0.1674 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 12288 × 768 × 3072 | Native | 0.3368 | 0.3368 | 1.0000 | 0.1666 | native_won_screening |
| 12288 × 3072 × 768 | Native | 0.3260 | 0.3260 | 1.0000 | 0.1664 | native_won_screening |
| 2047 × 4096 × 4096 | Native | 0.3405 | 0.3405 | 1.0000 | 0.1671 | native_won_screening |
| 2048 × 8191 × 2048 | Native | 0.3540 | 0.3540 | 1.0000 | 0.1674 | native_won_screening |
| 512 × 4096 × 16384 | S1 outputs; [512, 512, 4096]; b2 | 0.3539 | 0.3452 | 1.0250 | 0.4733 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 512 × 16384 × 4096 | Native | 0.3602 | 0.3602 | 1.0000 | 0.1673 | native_won_screening |
| 2048 × 1024 × 16384 | S1 products; [2048, 1024, 1024]; b2 | 0.3431 | 0.3195 | 1.0741 | 0.4758 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 4096 × 512 × 16384 | Native | 0.3393 | 0.3393 | 1.0000 | 0.1672 | native_won_screening |
| 4096 × 16384 × 512 | Native | 0.3520 | 0.3520 | 1.0000 | 0.1675 | native_won_screening |
| 16384 × 512 × 4096 | Native | 0.3456 | 0.3456 | 1.0000 | 0.1669 | native_won_screening |
| 16384 × 4096 × 512 | Native | 0.3524 | 0.3524 | 1.0000 | 0.1681 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 2048 × 8193 × 2048 | Native | 0.3405 | 0.3405 | 1.0000 | 0.1672 | native_won_screening |
| 2049 × 4096 × 4096 | Native | 0.3389 | 0.3389 | 1.0000 | 0.1669 | native_won_screening |
| 768 × 8192 × 6144 | Native | 0.3515 | 0.3515 | 1.0000 | 0.1673 | native_won_screening |
| 1536 × 384 × 65536 | Native | 0.4052 | 0.4052 | 1.0000 | 0.1662 | native_won_screening |
| 1536 × 16384 × 1536 | Native | 0.3579 | 0.3579 | 1.0000 | 0.1655 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 12288 × 1536 × 2048 | Native | 0.3696 | 0.3696 | 1.0000 | 0.1664 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 32768 × 1024 × 1536 | Native | 0.3618 | 0.3618 | 1.0000 | 0.1682 | native_won_screening |
| 49152 × 512 × 2048 | Native | 0.4076 | 0.4076 | 1.0000 | 0.1684 | native_won_screening |
| 49152 × 4096 × 256 | Native | 0.5272 | 0.5272 | 1.0000 | 0.1672 | native_won_screening |
| 98304 × 1024 × 512 | Native | 0.4570 | 0.4570 | 1.0000 | 0.1668 | native_won_screening |
| 4095 × 4095 × 4095 | Native | 0.4261 | 0.4261 | 1.0000 | 0.1670 | native_won_screening |
| 2048 × 4096 × 8191 | Native | 0.4106 | 0.4106 | 1.0000 | 0.1674 | native_won_screening |
| 2048 × 2048 × 16384 | Native | 0.4478 | 0.4478 | 1.0000 | 0.1676 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 2048 × 16384 × 2048 | Native | 0.4239 | 0.4239 | 1.0000 | 0.1671 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4096 × 4096 × 4096 | Native | 0.4161 | 0.4161 | 1.0000 | 0.1673 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 16384 × 2048 × 2048 | S1 products; [2048, 2048, 2048]; b2 | 0.4412 | 0.4064 | 1.0856 | 0.4775 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 2048 × 4096 × 8193 | Native | 0.4210 | 0.4210 | 1.0000 | 0.1673 | native_won_screening |
| 4097 × 4097 × 4097 | Native | 0.4538 | 0.4538 | 1.0000 | 0.1677 | native_won_screening |
| 1536 × 32768 × 1536 | Native | 0.4249 | 0.4249 | 1.0000 | 0.1674 | native_won_screening |
| 3072 × 8192 × 3072 | Native | 0.4733 | 0.4733 | 1.0000 | 0.1678 | native_won_screening |
| 4608 × 4608 × 4608 | Native | 0.5036 | 0.5036 | 1.0000 | 0.1665 | native_won_screening |
| 256 × 98304 × 4096 | Native | 0.8072 | 0.8072 | 1.0000 | 0.1663 | native_won_screening |
| 512 × 16384 × 12288 | Native | 0.5466 | 0.5466 | 1.0000 | 0.1688 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 16384 × 1024 × 6144 | S1 products; [4096, 1024, 1024]; b2 | 0.4970 | 0.4737 | 1.0492 | 0.4735 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 65536 × 256 × 6144 | Native | 0.7869 | 0.7869 | 1.0000 | 0.1663 | native_won_screening |
| 768 × 24576 × 6144 | Native | 0.5679 | 0.5679 | 1.0000 | 0.1674 | native_won_screening |
| 5120 × 5120 × 5120 | Native | 0.5725 | 0.5725 | 1.0000 | 0.1674 | native_won_screening |
| 256 × 32768 × 16384 | Native | 0.9547 | 0.9547 | 1.0000 | 0.1680 | native_won_screening |
| 2048 × 2048 × 32768 | S1 products; [2048, 2048, 2048]; b2 | 0.5805 | 0.5504 | 1.0546 | 0.4743 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 2048 × 32768 × 2048 | S1 outputs; [2048, 2048, 1024]; b2 | 0.5771 | 0.5548 | 1.0401 | 0.4707 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 32768 × 2048 × 2048 | S1 outputs; [2048, 2048, 2048]; b2 | 0.5717 | 0.5403 | 1.0581 | 0.4730 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 131072 × 1024 × 1024 | S1 products; [2048, 1024, 1024]; b2 | 0.6362 | 0.6292 | 1.0111 | 0.4748 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 1536 × 24576 × 4096 | Native | 0.6572 | 0.6572 | 1.0000 | 0.1655 | native_won_screening |
| 1536 × 65536 × 1536 | Native | 0.6115 | 0.6115 | 1.0000 | 0.1669 | native_won_screening |
| 3072 × 16384 × 3072 | Native | 0.6237 | 0.6237 | 1.0000 | 0.1664 | native_won_screening |
| 2048 × 32768 × 3072 | S1 products; [2048, 1024, 1024]; b2 | 0.7370 | 0.7219 | 1.0209 | 0.4774 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 3072 × 32768 × 2048 | Native | 0.7485 | 0.7485 | 1.0000 | 0.1667 | native_won_screening |
| 4096 × 2048 × 24576 | S1 outputs; [2048, 2048, 2048]; b2 | 0.7249 | 0.6779 | 1.0694 | 0.4731 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 4096 × 131072 × 384 | Native | 1.0306 | 1.0306 | 1.0000 | 0.1665 | native_won_screening |
| 768 × 49152 × 6144 | Native | 0.8034 | 0.8034 | 1.0000 | 0.1677 | native_won_screening |
| 2048 × 2048 × 65536 | S1 outputs; [2048, 2048, 2048]; b2 | 0.8974 | 0.8330 | 1.0773 | 0.4715 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 2048 × 65536 × 2048 | Native | 0.8928 | 0.8928 | 1.0000 | 0.1675 | frozen_winner_did_not_clear_1_percent_mean_margin |
| 4096 × 8192 × 8192 | S1 outputs; [2048, 2048, 4096]; b2 | 0.9181 | 0.8749 | 1.0493 | 0.4750 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 4096 × 16384 × 4096 | Native | 0.9258 | 0.9258 | 1.0000 | 0.1662 | frozen_winner_speedup_not_resolved_by_paired_95_percent_interval |
| 8192 × 4096 × 8192 | S1 outputs; [2048, 2048, 4096]; b2 | 0.8864 | 0.8338 | 1.0631 | 0.4724 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 8192 × 8192 × 4096 | S1 outputs; [2048, 2048, 4096]; b2 | 0.9185 | 0.8703 | 1.0554 | 0.4756 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 65536 × 2048 × 2048 | S1 outputs; [2048, 2048, 2048]; b2 | 0.8913 | 0.8378 | 1.0638 | 0.4688 | frozen_winner_passed_errors_and_confirmed_speed_margin |
| 384 × 12288 × 65536 | Native | 1.3404 | 1.3404 | 1.0000 | 0.1669 | native_won_screening |
| 384 × 65536 × 12288 | Native | 1.3638 | 1.3638 | 1.0000 | 0.1663 | native_won_screening |
| 1536 × 131072 × 1536 | Native | 0.9855 | 0.9855 | 1.0000 | 0.1661 | native_won_screening |
| 8192 × 8192 × 8192 | S1 outputs; [2048, 2048, 4096]; b2 | 1.6031 | 1.4979 | 1.0702 | 0.4744 | frozen_winner_passed_errors_and_confirmed_speed_margin |

## All five method timings

| Shape | Output | Default Native ms | Tuned Native ms | Cubic ms | S1 ms | S2 ms |
|---|---|---:|---:|---:|---:|---:|
| shape_m1_k1_n1 | float32 | 0.2275 | 0.2283 | 0.2329 | 0.2277 | 0.2330 |
| shape_m1_k1_n1 | bfloat16 | 0.2659 | 0.2448 | 0.2440 | 0.2406 | 0.2532 |
| shape_m3_k3_n3 | float32 | 0.2432 | 0.2416 | 0.2470 | 0.2434 | 0.2415 |
| shape_m3_k3_n3 | bfloat16 | 0.2472 | 0.2481 | 0.2459 | 0.2445 | 0.2442 |
| shape_m16_k16_n16 | float32 | 0.2172 | 0.2197 | 0.2174 | 0.2177 | 0.2201 |
| shape_m16_k16_n16 | bfloat16 | 0.2388 | 0.2433 | 0.2402 | 0.2398 | 0.2390 |
| shape_m64_k64_n64 | float32 | 0.2184 | 0.2203 | 0.2200 | 0.2154 | 0.2196 |
| shape_m64_k64_n64 | bfloat16 | 0.2178 | 0.2205 | 0.2171 | 0.2188 | 0.2177 |
| shape_m128_k128_n128 | float32 | 0.2267 | 0.2284 | 0.2285 | 0.2293 | 0.2278 |
| shape_m128_k128_n128 | bfloat16 | 0.2384 | 0.2387 | 0.2399 | 0.2395 | 0.2386 |
| shape_m256_k256_n256 | float32 | 0.2191 | 0.2191 | 0.2185 | 0.2191 | 0.2218 |
| shape_m256_k256_n256 | bfloat16 | 0.2237 | 0.2237 | 0.2202 | 0.2227 | 0.2258 |
| shape_m8_k2048_n2048 | float32 | 0.2233 | 0.2253 | 0.2259 | 0.2316 | 0.2290 |
| shape_m8_k2048_n2048 | bfloat16 | 0.2325 | 0.2333 | 0.2355 | 0.2354 | 0.2346 |
| shape_m2048_k8_n2048 | float32 | 0.2275 | 0.2267 | 0.2274 | 0.2283 | 0.2364 |
| shape_m2048_k8_n2048 | bfloat16 | 0.2484 | 0.2517 | 0.2488 | 0.2505 | 0.2538 |
| shape_m2048_k2048_n8 | float32 | 0.2277 | 0.2290 | 0.2289 | 0.2279 | 0.2460 |
| shape_m2048_k2048_n8 | bfloat16 | 0.2326 | 0.2308 | 0.2337 | 0.2330 | 0.2374 |
| shape_m384_k384_n384 | float32 | 0.2265 | 0.2286 | 0.2320 | 0.2252 | 0.2276 |
| shape_m384_k384_n384 | bfloat16 | 0.2411 | 0.2455 | 0.2479 | 0.2440 | 0.2429 |
| shape_m384_k1024_n256 | float32 | 0.2367 | 0.2417 | 0.2335 | 0.2331 | 0.2499 |
| shape_m384_k1024_n256 | bfloat16 | 0.2355 | 0.2341 | 0.2437 | 0.2344 | 0.2480 |
| shape_m512_k512_n512 | float32 | 0.2385 | 0.2397 | 0.2432 | 0.2410 | 0.2386 |
| shape_m512_k512_n512 | bfloat16 | 0.2486 | 0.2469 | 0.2503 | 0.2464 | 0.2523 |
| shape_m256_k1024_n768 | float32 | 0.2588 | 0.2590 | 0.2559 | 0.2576 | 0.2583 |
| shape_m256_k1024_n768 | bfloat16 | 0.2540 | 0.2547 | 0.2506 | 0.2762 | 0.2754 |
| shape_m512_k512_n768 | float32 | 0.2425 | 0.2265 | 0.2247 | 0.2267 | 0.2264 |
| shape_m512_k512_n768 | bfloat16 | 0.2383 | 0.2394 | 0.2429 | 0.2438 | 0.2444 |
| shape_m384_k1536_n512 | float32 | 0.2229 | 0.2245 | 0.2267 | 0.2407 | 0.2241 |
| shape_m384_k1536_n512 | bfloat16 | 0.2294 | 0.2342 | 0.2294 | 0.2369 | 0.2316 |
| shape_m512_k2048_n384 | float32 | 0.2455 | 0.2459 | 0.2460 | 0.2463 | 0.2467 |
| shape_m512_k2048_n384 | bfloat16 | 0.2402 | 0.2411 | 0.2435 | 0.2365 | 0.2402 |
| shape_m512_k3072_n256 | float32 | 0.2368 | 0.2376 | 0.2381 | 0.2396 | 0.2429 |
| shape_m512_k3072_n256 | bfloat16 | 0.2359 | 0.2389 | 0.2402 | 0.2383 | 0.2410 |
| shape_m768_k768_n768 | float32 | 0.2442 | 0.2415 | 0.2494 | 0.2454 | 0.2422 |
| shape_m768_k768_n768 | bfloat16 | 0.2449 | 0.2450 | 0.2443 | 0.2482 | 0.2475 |
| shape_m512_k6144_n256 | float32 | 0.2254 | 0.2260 | 0.2276 | 0.2258 | 0.2315 |
| shape_m512_k6144_n256 | bfloat16 | 0.2142 | 0.2171 | 0.2193 | 0.2181 | 0.2201 |
| shape_m1536_k2048_n256 | float32 | 0.2428 | 0.2398 | 0.2496 | 0.2413 | 0.2468 |
| shape_m1536_k2048_n256 | bfloat16 | 0.2393 | 0.2410 | 0.2428 | 0.2420 | 0.2435 |
| shape_m1023_k1023_n1023 | float32 | 0.2368 | 0.2368 | 0.2392 | 0.2381 | 0.2409 |
| shape_m1023_k1023_n1023 | bfloat16 | 0.2479 | 0.2479 | 0.2505 | 0.2493 | 0.2509 |
| shape_m64_k512_n32768 | float32 | 0.2559 | 0.2558 | 0.2914 | 0.2913 | 0.3023 |
| shape_m64_k512_n32768 | bfloat16 | 0.2619 | 0.2619 | 0.2820 | 0.2858 | 0.2909 |
| shape_m256_k2048_n2048 | float32 | 0.2250 | 0.2273 | 0.2297 | 0.2254 | 0.2320 |
| shape_m256_k2048_n2048 | bfloat16 | 0.2309 | 0.2328 | 0.2398 | 0.2311 | 0.2342 |
| shape_m1024_k1024_n1024 | float32 | 0.2378 | 0.2377 | 0.2334 | 0.2350 | 0.2382 |
| shape_m1024_k1024_n1024 | bfloat16 | 0.2392 | 0.2358 | 0.2339 | 0.2367 | 0.2369 |
| shape_m2048_k256_n2048 | float32 | 0.2344 | 0.2344 | 0.2403 | 0.2319 | 0.2402 |
| shape_m2048_k256_n2048 | bfloat16 | 0.2400 | 0.2400 | 0.2404 | 0.2397 | 0.2455 |
| shape_m2048_k2048_n256 | float32 | 0.2411 | 0.2411 | 0.2398 | 0.2419 | 0.2430 |
| shape_m2048_k2048_n256 | bfloat16 | 0.2384 | 0.2384 | 0.2416 | 0.2367 | 0.2431 |
| shape_m32768_k512_n64 | float32 | 0.2426 | 0.2426 | 0.3052 | 0.3018 | 0.3089 |
| shape_m32768_k512_n64 | bfloat16 | 0.2527 | 0.2616 | 0.2896 | 0.2936 | 0.3063 |
| shape_m1025_k1025_n1025 | float32 | 0.2389 | 0.2389 | 0.2678 | 0.2654 | 0.2703 |
| shape_m1025_k1025_n1025 | bfloat16 | 0.2342 | 0.2342 | 0.2567 | 0.2513 | 0.2515 |
| shape_m256_k6144_n768 | float32 | 0.2485 | 0.2510 | 0.2545 | 0.2585 | 0.2724 |
| shape_m256_k6144_n768 | bfloat16 | 0.2380 | 0.2398 | 0.2460 | 0.2470 | 0.2514 |
| shape_m1536_k1024_n768 | float32 | 0.2444 | 0.2367 | 0.2396 | 0.2450 | 0.2416 |
| shape_m1536_k1024_n768 | bfloat16 | 0.2358 | 0.2365 | 0.2388 | 0.2385 | 0.2400 |
| shape_m384_k3072_n2048 | float32 | 0.2491 | 0.2551 | 0.2524 | 0.2568 | 0.2618 |
| shape_m384_k3072_n2048 | bfloat16 | 0.2530 | 0.2530 | 0.2534 | 0.2540 | 0.2621 |
| shape_m384_k16384_n384 | float32 | 0.2509 | 0.2526 | 0.2786 | 0.2865 | 0.3039 |
| shape_m384_k16384_n384 | bfloat16 | 0.2568 | 0.2547 | 0.2872 | 0.2889 | 0.3104 |
| shape_m256_k2048_n6144 | float32 | 0.2402 | 0.2347 | 0.2327 | 0.2368 | 0.2436 |
| shape_m256_k2048_n6144 | bfloat16 | 0.2471 | 0.2413 | 0.2409 | 0.2422 | 0.2610 |
| shape_m4096_k1536_n512 | float32 | 0.2367 | 0.2355 | 0.2360 | 0.2369 | 0.2587 |
| shape_m4096_k1536_n512 | bfloat16 | 0.2456 | 0.2485 | 0.2439 | 0.2407 | 0.2656 |
| shape_m32768_k256_n384 | float32 | 0.2817 | 0.2817 | 0.4177 | 0.4146 | 0.4203 |
| shape_m32768_k256_n384 | bfloat16 | 0.2620 | 0.2609 | 0.3625 | 0.3762 | 0.3774 |
| shape_m384_k1536_n12288 | float32 | 0.2753 | 0.2752 | 0.3032 | 0.3044 | 0.3195 |
| shape_m384_k1536_n12288 | bfloat16 | 0.2644 | 0.2668 | 0.2636 | 0.2612 | 0.2842 |
| shape_m2048_k2048_n2048 | float32 | 0.2640 | 0.2680 | 0.2733 | 0.2729 | 0.2836 |
| shape_m2048_k2048_n2048 | bfloat16 | 0.2482 | 0.2525 | 0.2719 | 0.2530 | 0.2532 |
| shape_m256_k1536_n24576 | float32 | 0.3096 | 0.3114 | 0.3059 | 0.3082 | 0.3296 |
| shape_m256_k1536_n24576 | bfloat16 | 0.3021 | 0.3032 | 0.2941 | 0.2985 | 0.3179 |
| shape_m384_k6144_n4096 | float32 | 0.2941 | 0.2966 | 0.2801 | 0.2802 | 0.3222 |
| shape_m384_k6144_n4096 | bfloat16 | 0.2971 | 0.2953 | 0.2815 | 0.2872 | 0.3240 |
| shape_m256_k16384_n4096 | float32 | 0.3305 | 0.3305 | 0.3340 | 0.3380 | 0.3947 |
| shape_m256_k16384_n4096 | bfloat16 | 0.3297 | 0.3297 | 0.3304 | 0.3335 | 0.3885 |
| shape_m4096_k256_n16384 | float32 | 0.4088 | 0.4088 | 0.4420 | 0.4421 | 0.4606 |
| shape_m4096_k256_n16384 | bfloat16 | 0.3301 | 0.3331 | 0.3632 | 0.3642 | 0.4320 |
| shape_m16384_k256_n4096 | float32 | 0.4067 | 0.4061 | 0.4345 | 0.4354 | 0.4562 |
| shape_m16384_k256_n4096 | bfloat16 | 0.3185 | 0.3194 | 0.3651 | 0.3635 | 0.4284 |
| shape_m256_k24576_n3072 | float32 | 0.3505 | 0.3505 | 0.3514 | 0.3514 | 0.4120 |
| shape_m256_k24576_n3072 | bfloat16 | 0.3327 | 0.3327 | 0.3374 | 0.3386 | 0.3961 |
| shape_m256_k49152_n1536 | float32 | 0.3539 | 0.3466 | 0.3933 | 0.3891 | 0.4135 |
| shape_m256_k49152_n1536 | bfloat16 | 0.3515 | 0.3458 | 0.3915 | 0.3855 | 0.4110 |
| shape_m384_k384_n131072 | float32 | 0.4526 | 0.4479 | 1.0130 | 1.0040 | 1.0477 |
| shape_m384_k384_n131072 | bfloat16 | 0.3764 | 0.3731 | 0.8017 | 0.7956 | 0.8598 |
| shape_m1536_k8192_n1536 | float32 | 0.3069 | 0.3038 | 0.3174 | 0.3145 | 0.3599 |
| shape_m1536_k8192_n1536 | bfloat16 | 0.3091 | 0.2956 | 0.3198 | 0.3177 | 0.3659 |
| shape_m6144_k2048_n1536 | float32 | 0.2845 | 0.2855 | 0.2959 | 0.2968 | 0.3167 |
| shape_m6144_k2048_n1536 | bfloat16 | 0.2917 | 0.2930 | 0.2950 | 0.2913 | 0.3198 |
| shape_m768_k3072_n12288 | float32 | 0.3864 | 0.3864 | 0.4078 | 0.4114 | 0.4352 |
| shape_m768_k3072_n12288 | bfloat16 | 0.3537 | 0.3122 | 0.3615 | 0.3512 | 0.3956 |
| shape_m768_k12288_n3072 | float32 | 0.3912 | 0.3444 | 0.4294 | 0.4102 | 0.4290 |
| shape_m768_k12288_n3072 | bfloat16 | 0.3954 | 0.3430 | 0.4212 | 0.4200 | 0.4315 |
| shape_m3072_k768_n12288 | float32 | 0.5040 | 0.5040 | 0.5968 | 0.6063 | 0.5769 |
| shape_m3072_k768_n12288 | bfloat16 | 0.3519 | 0.3519 | 0.4210 | 0.4234 | 0.4368 |
| shape_m3072_k12288_n768 | float32 | 0.4038 | 0.3634 | 0.4324 | 0.4287 | 0.4515 |
| shape_m3072_k12288_n768 | bfloat16 | 0.3647 | 0.3647 | 0.4209 | 0.3965 | 0.4966 |
| shape_m12288_k768_n3072 | float32 | 0.3366 | 0.3349 | 0.3845 | 0.3821 | 0.4249 |
| shape_m12288_k768_n3072 | bfloat16 | 0.3322 | 0.3368 | 0.4089 | 0.3793 | 0.4084 |
| shape_m12288_k3072_n768 | float32 | 0.3731 | 0.3458 | 0.4371 | 0.4087 | 0.4995 |
| shape_m12288_k3072_n768 | bfloat16 | 0.3623 | 0.3260 | 0.3783 | 0.3690 | 0.3849 |
| shape_m2047_k4096_n4096 | float32 | 0.3517 | 0.3517 | 0.3907 | 0.3577 | 0.3691 |
| shape_m2047_k4096_n4096 | bfloat16 | 0.3461 | 0.3405 | 0.3634 | 0.3581 | 0.3643 |
| shape_m2048_k8191_n2048 | float32 | 0.3498 | 0.3370 | 0.4293 | 0.4369 | 0.4632 |
| shape_m2048_k8191_n2048 | bfloat16 | 0.3441 | 0.3540 | 0.4410 | 0.4694 | 0.5138 |
| shape_m512_k4096_n16384 | float32 | 0.3572 | 0.3531 | 0.3499 | 0.3468 | 0.4275 |
| shape_m512_k4096_n16384 | bfloat16 | 0.3543 | 0.3539 | 0.3495 | 0.3452 | 0.4335 |
| shape_m512_k16384_n4096 | float32 | 0.3609 | 0.3554 | 0.3580 | 0.3550 | 0.4429 |
| shape_m512_k16384_n4096 | bfloat16 | 0.3694 | 0.3602 | 0.3618 | 0.3568 | 0.4474 |
| shape_m2048_k1024_n16384 | float32 | 0.3757 | 0.3719 | 0.3658 | 0.3673 | 0.3726 |
| shape_m2048_k1024_n16384 | bfloat16 | 0.3469 | 0.3431 | 0.3288 | 0.3195 | 0.3460 |
| shape_m4096_k512_n16384 | float32 | 0.4110 | 0.4148 | 0.4381 | 0.4200 | 0.4409 |
| shape_m4096_k512_n16384 | bfloat16 | 0.3479 | 0.3393 | 0.3316 | 0.3331 | 0.4055 |
| shape_m4096_k16384_n512 | float32 | 0.3458 | 0.3474 | 0.3478 | 0.3512 | 0.3991 |
| shape_m4096_k16384_n512 | bfloat16 | 0.3524 | 0.3520 | 0.3498 | 0.3502 | 0.3994 |
| shape_m16384_k512_n4096 | float32 | 0.4601 | 0.4344 | 0.4453 | 0.4447 | 0.4617 |
| shape_m16384_k512_n4096 | bfloat16 | 0.3478 | 0.3456 | 0.3529 | 0.3522 | 0.4166 |
| shape_m16384_k4096_n512 | float32 | 0.3638 | 0.3590 | 0.3645 | 0.3631 | 0.3959 |
| shape_m16384_k4096_n512 | bfloat16 | 0.3622 | 0.3524 | 0.3508 | 0.3507 | 0.4001 |
| shape_m2048_k8193_n2048 | float32 | 0.3657 | 0.3540 | 0.4451 | 0.4495 | 0.4880 |
| shape_m2048_k8193_n2048 | bfloat16 | 0.3774 | 0.3405 | 0.4522 | 0.4364 | 0.4770 |
| shape_m2049_k4096_n4096 | float32 | 0.3668 | 0.3664 | 0.4767 | 0.4726 | 0.4955 |
| shape_m2049_k4096_n4096 | bfloat16 | 0.3389 | 0.3389 | 0.4340 | 0.4173 | 0.4442 |
| shape_m768_k8192_n6144 | float32 | 0.3518 | 0.3448 | 0.4279 | 0.4135 | 0.4570 |
| shape_m768_k8192_n6144 | bfloat16 | 0.3764 | 0.3515 | 0.4133 | 0.3999 | 0.4381 |
| shape_m1536_k384_n65536 | float32 | 0.5262 | 0.5262 | 0.8060 | 0.8057 | 0.8657 |
| shape_m1536_k384_n65536 | bfloat16 | 0.3845 | 0.4052 | 0.7197 | 0.7062 | 0.7928 |
| shape_m1536_k16384_n1536 | float32 | 0.3760 | 0.3742 | 0.3971 | 0.3957 | 0.4761 |
| shape_m1536_k16384_n1536 | bfloat16 | 0.3592 | 0.3579 | 0.3806 | 0.4447 | 0.5597 |
| shape_m12288_k1536_n2048 | float32 | 0.3586 | 0.3661 | 0.3620 | 0.3461 | 0.3868 |
| shape_m12288_k1536_n2048 | bfloat16 | 0.3680 | 0.3696 | 0.3559 | 0.3540 | 0.3786 |
| shape_m32768_k1024_n1536 | float32 | 0.4250 | 0.4250 | 0.5473 | 0.5427 | 0.5696 |
| shape_m32768_k1024_n1536 | bfloat16 | 0.3959 | 0.3618 | 0.4557 | 0.4504 | 0.5211 |
| shape_m49152_k512_n2048 | float32 | 0.5222 | 0.5367 | 0.5432 | 0.5403 | 0.5498 |
| shape_m49152_k512_n2048 | bfloat16 | 0.4095 | 0.4076 | 0.4099 | 0.4128 | 0.5093 |
| shape_m49152_k4096_n256 | float32 | 0.5450 | 0.5439 | 0.6807 | 0.6732 | 0.7879 |
| shape_m49152_k4096_n256 | bfloat16 | 0.5272 | 0.5272 | 0.5907 | 0.5901 | 0.7427 |
| shape_m98304_k1024_n512 | float32 | 0.5115 | 0.5119 | 0.5496 | 0.5142 | 0.5427 |
| shape_m98304_k1024_n512 | bfloat16 | 0.4818 | 0.4570 | 0.4801 | 0.4625 | 0.5118 |
| shape_m4095_k4095_n4095 | float32 | 0.4382 | 0.4322 | 0.5352 | 0.5152 | 0.5262 |
| shape_m4095_k4095_n4095 | bfloat16 | 0.4324 | 0.4261 | 0.5195 | 0.5028 | 0.5245 |
| shape_m2048_k4096_n8191 | float32 | 0.4750 | 0.4243 | 0.5568 | 0.5126 | 0.5647 |
| shape_m2048_k4096_n8191 | bfloat16 | 0.4490 | 0.4106 | 0.5092 | 0.4917 | 0.5082 |
| shape_m2048_k2048_n16384 | float32 | 0.4733 | 0.4221 | 0.4196 | 0.4061 | 0.4683 |
| shape_m2048_k2048_n16384 | bfloat16 | 0.4792 | 0.4478 | 0.4263 | 0.4427 | 0.4432 |
| shape_m2048_k16384_n2048 | float32 | 0.4652 | 0.4389 | 0.4241 | 0.4251 | 0.4331 |
| shape_m2048_k16384_n2048 | bfloat16 | 0.4701 | 0.4239 | 0.4612 | 0.4533 | 0.4400 |
| shape_m4096_k4096_n4096 | float32 | 0.4351 | 0.4281 | 0.4428 | 0.4397 | 0.4408 |
| shape_m4096_k4096_n4096 | bfloat16 | 0.4287 | 0.4161 | 0.4245 | 0.4260 | 0.4227 |
| shape_m16384_k2048_n2048 | float32 | 0.4475 | 0.4475 | 0.4081 | 0.4063 | 0.4313 |
| shape_m16384_k2048_n2048 | bfloat16 | 0.4412 | 0.4412 | 0.4012 | 0.4064 | 0.4152 |
| shape_m2048_k4096_n8193 | float32 | 0.4778 | 0.4422 | 0.6785 | 0.6741 | 0.7084 |
| shape_m2048_k4096_n8193 | bfloat16 | 0.4611 | 0.4210 | 0.6244 | 0.6045 | 0.6264 |
| shape_m4097_k4097_n4097 | float32 | 0.4538 | 0.4579 | 0.8366 | 0.8216 | 0.9134 |
| shape_m4097_k4097_n4097 | bfloat16 | 0.4515 | 0.4538 | 0.8155 | 0.7631 | 0.8410 |
| shape_m1536_k32768_n1536 | float32 | 0.4357 | 0.4356 | 0.6413 | 0.6498 | 0.6905 |
| shape_m1536_k32768_n1536 | bfloat16 | 0.4260 | 0.4249 | 0.6292 | 0.6302 | 0.6664 |
| shape_m3072_k8192_n3072 | float32 | 0.4669 | 0.4648 | 0.4815 | 0.4767 | 0.5048 |
| shape_m3072_k8192_n3072 | bfloat16 | 0.4789 | 0.4733 | 0.4750 | 0.4598 | 0.4987 |
| shape_m4608_k4608_n4608 | float32 | 0.4943 | 0.5108 | 0.6111 | 0.6048 | 0.7795 |
| shape_m4608_k4608_n4608 | bfloat16 | 0.5027 | 0.5036 | 0.5873 | 0.5787 | 0.7707 |
| shape_m256_k98304_n4096 | float32 | 0.7916 | 0.8062 | 1.0552 | 1.0422 | 1.1314 |
| shape_m256_k98304_n4096 | bfloat16 | 0.7970 | 0.8072 | 1.0608 | 1.0490 | 1.1247 |
| shape_m512_k16384_n12288 | float32 | 0.5692 | 0.5547 | 0.5635 | 0.5553 | 0.7930 |
| shape_m512_k16384_n12288 | bfloat16 | 0.5639 | 0.5466 | 0.5479 | 0.5456 | 0.7995 |
| shape_m16384_k1024_n6144 | float32 | 0.5461 | 0.5461 | 0.5770 | 0.5779 | 0.5990 |
| shape_m16384_k1024_n6144 | bfloat16 | 0.4997 | 0.4970 | 0.4918 | 0.4737 | 0.5279 |
| shape_m65536_k256_n6144 | float32 | 1.3056 | 1.2979 | 1.3881 | 1.3909 | 1.4597 |
| shape_m65536_k256_n6144 | bfloat16 | 0.7934 | 0.7869 | 0.9087 | 0.9178 | 1.3404 |
| shape_m768_k24576_n6144 | float32 | 0.5647 | 0.5568 | 0.8194 | 0.7165 | 0.8016 |
| shape_m768_k24576_n6144 | bfloat16 | 0.5679 | 0.5679 | 0.7190 | 0.6779 | 0.7402 |
| shape_m5120_k5120_n5120 | float32 | 0.5980 | 0.5945 | 0.6002 | 0.5728 | 0.6389 |
| shape_m5120_k5120_n5120 | bfloat16 | 0.5896 | 0.5725 | 0.5651 | 0.5376 | 0.6052 |
| shape_m256_k32768_n16384 | float32 | 0.9526 | 0.9526 | 0.9965 | 0.9800 | 1.3837 |
| shape_m256_k32768_n16384 | bfloat16 | 0.9547 | 0.9547 | 0.9672 | 0.9772 | 1.4091 |
| shape_m2048_k2048_n32768 | float32 | 0.5815 | 0.5716 | 2.6507 | 0.5693 | 0.5998 |
| shape_m2048_k2048_n32768 | bfloat16 | 0.5794 | 0.5805 | 0.5759 | 0.5504 | 0.5987 |
| shape_m2048_k32768_n2048 | float32 | 0.5803 | 0.5770 | 0.5757 | 0.5447 | 0.6111 |
| shape_m2048_k32768_n2048 | bfloat16 | 0.6068 | 0.5771 | 0.5977 | 0.5548 | 0.6124 |
| shape_m32768_k2048_n2048 | float32 | 0.5825 | 0.5773 | 0.5789 | 0.5619 | 0.6137 |
| shape_m32768_k2048_n2048 | bfloat16 | 0.5717 | 0.5717 | 0.5669 | 0.5403 | 0.5862 |
| shape_m131072_k1024_n1024 | float32 | 0.8057 | 0.8039 | 0.8059 | 0.8009 | 0.8072 |
| shape_m131072_k1024_n1024 | bfloat16 | 0.6362 | 0.6362 | 0.6315 | 0.6292 | 0.6534 |
| shape_m1536_k24576_n4096 | float32 | 0.6428 | 0.6532 | 0.7156 | 0.7098 | 0.8915 |
| shape_m1536_k24576_n4096 | bfloat16 | 0.6451 | 0.6572 | 0.7128 | 0.7066 | 0.8696 |
| shape_m1536_k65536_n1536 | float32 | 0.6353 | 0.6274 | 1.0596 | 1.0474 | 1.0911 |
| shape_m1536_k65536_n1536 | bfloat16 | 0.6193 | 0.6115 | 1.0329 | 1.0318 | 1.0783 |
| shape_m3072_k16384_n3072 | float32 | 0.6666 | 0.6296 | 0.6741 | 0.6412 | 0.7288 |
| shape_m3072_k16384_n3072 | bfloat16 | 0.6600 | 0.6237 | 0.6712 | 0.6385 | 0.7185 |
| shape_m2048_k32768_n3072 | float32 | 0.7874 | 0.7408 | 0.7707 | 0.7243 | 0.8526 |
| shape_m2048_k32768_n3072 | bfloat16 | 0.7902 | 0.7370 | 0.8169 | 0.7219 | 0.8443 |
| shape_m3072_k32768_n2048 | float32 | 0.7851 | 0.7416 | 0.7805 | 0.7632 | 0.8481 |
| shape_m3072_k32768_n2048 | bfloat16 | 0.7893 | 0.7485 | 0.8230 | 0.7597 | 0.8455 |
| shape_m4096_k2048_n24576 | float32 | 0.7563 | 0.7536 | 0.7536 | 0.7236 | 0.7681 |
| shape_m4096_k2048_n24576 | bfloat16 | 0.7366 | 0.7249 | 0.7217 | 0.6779 | 0.7280 |
| shape_m4096_k131072_n384 | float32 | 1.0635 | 1.0184 | 1.5706 | 1.5294 | 1.8616 |
| shape_m4096_k131072_n384 | bfloat16 | 1.0658 | 1.0306 | 1.5703 | 1.5368 | 1.8605 |
| shape_m768_k49152_n6144 | float32 | 0.8716 | 0.8077 | 1.1749 | 1.1555 | 1.3541 |
| shape_m768_k49152_n6144 | bfloat16 | 0.8657 | 0.8034 | 1.1739 | 1.1273 | 1.3347 |
| shape_m2048_k2048_n65536 | float32 | 0.9113 | 0.8981 | 0.8930 | 0.8535 | 0.9618 |
| shape_m2048_k2048_n65536 | bfloat16 | 0.9091 | 0.8974 | 0.8818 | 0.8330 | 0.9434 |
| shape_m2048_k65536_n2048 | float32 | 0.9120 | 0.8846 | 0.8932 | 0.8300 | 0.9591 |
| shape_m2048_k65536_n2048 | bfloat16 | 0.9631 | 0.8928 | 0.9977 | 0.9490 | 0.9704 |
| shape_m4096_k8192_n8192 | float32 | 0.9624 | 0.9624 | 0.9310 | 0.8881 | 0.9420 |
| shape_m4096_k8192_n8192 | bfloat16 | 0.9665 | 0.9181 | 0.9333 | 0.8749 | 0.8780 |
| shape_m4096_k16384_n4096 | float32 | 1.0038 | 0.9186 | 1.1219 | 0.8779 | 0.9315 |
| shape_m4096_k16384_n4096 | bfloat16 | 1.0069 | 0.9258 | 0.9758 | 0.9010 | 0.9231 |
| shape_m8192_k4096_n8192 | float32 | 0.9577 | 0.9383 | 0.9310 | 0.8738 | 0.9308 |
| shape_m8192_k4096_n8192 | bfloat16 | 0.9281 | 0.8864 | 0.8833 | 0.8338 | 0.9123 |
| shape_m8192_k8192_n4096 | float32 | 1.0552 | 0.9366 | 0.9330 | 0.8916 | 0.9424 |
| shape_m8192_k8192_n4096 | bfloat16 | 0.9731 | 0.9185 | 0.9553 | 0.8703 | 0.8763 |
| shape_m65536_k2048_n2048 | float32 | 0.9213 | 0.9007 | 0.8997 | 0.8741 | 0.9687 |
| shape_m65536_k2048_n2048 | bfloat16 | 0.9092 | 0.8913 | 0.8871 | 0.8378 | 0.9179 |
| shape_m384_k12288_n65536 | float32 | 1.3623 | 1.3623 | 1.5425 | 1.5404 | 2.5716 |
| shape_m384_k12288_n65536 | bfloat16 | 1.3404 | 1.3404 | 1.4360 | 1.4219 | 2.4840 |
| shape_m384_k65536_n12288 | float32 | 1.3602 | 1.3628 | 2.4747 | 2.4868 | 2.5553 |
| shape_m384_k65536_n12288 | bfloat16 | 1.3638 | 1.3638 | 2.4614 | 2.4306 | 2.5184 |
| shape_m1536_k131072_n1536 | float32 | 1.0118 | 0.9945 | 2.1099 | 2.1001 | 2.4363 |
| shape_m1536_k131072_n1536 | bfloat16 | 1.0101 | 0.9855 | 2.0954 | 2.0964 | 2.4286 |
| shape_m8192_k8192_n8192 | float32 | 1.8067 | 1.5925 | 1.5889 | 1.4867 | 1.6003 |
| shape_m8192_k8192_n8192 | bfloat16 | 1.7772 | 1.6031 | 1.6133 | 1.4979 | 1.5131 |

## Why each depth chose its configuration

Counterfactuals below change only accumulator strategy or buffer count at the selected tile. A ratio above 1 favors the selected configuration. They help separate measured effects from memory-based hypotheses. Counterfactual failures remain visible.

### shape_m1_k1_n1__float32

- S1: S1 products; [32, 512, 512]; b2; confirmed 0.2277 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0099× [0.9836, 1.0358].
  - other_buffers: 1.0068× [0.9857, 1.0287].
- S2: S2 products; [256, 512, 512]; b2; confirmed 0.2330 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9851× [0.9426, 1.0180].
  - other_buffers: 0.9783× [0.9466, 1.0068].

### shape_m1_k1_n1__bfloat16

- S1: S1 products; [128, 512, 512]; b2; confirmed 0.2406 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0123× [0.9956, 1.0324].
  - other_buffers: 1.0922× [1.0004, 1.2900].
- S2: S2 products; [256, 512, 512]; b2; confirmed 0.2532 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9852× [0.8852, 1.0704].
  - other_buffers: 0.9590× [0.8576, 1.0175].

### shape_m3_k3_n3__float32

- S1: S1 products; [128, 512, 512]; b2; confirmed 0.2434 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9864× [0.9567, 1.0133].
  - other_buffers: 1.0067× [0.9642, 1.0628].
- S2: S2 outputs; [32, 512, 512]; b1; confirmed 0.2415 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9875, 1.0172].
  - other_buffers: 1.0000× [0.9830, 1.0185].

### shape_m3_k3_n3__bfloat16

- S1: S1 outputs; [128, 512, 512]; b1; confirmed 0.2445 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0086× [0.9936, 1.0266].
  - other_buffers: 1.0083× [0.9918, 1.0255].
- S2: S2 products; [128, 512, 512]; b2; confirmed 0.2442 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9902× [0.9720, 1.0068].
  - other_buffers: 1.0081× [0.9932, 1.0237].

### shape_m16_k16_n16__float32

- S1: S1 products; [32, 512, 512]; b2; confirmed 0.2177 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0070× [0.9878, 1.0266].
  - other_buffers: 1.0013× [0.9826, 1.0202].
- S2: S2 outputs; [128, 512, 512]; b1; confirmed 0.2201 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9914× [0.9691, 1.0099].
  - other_buffers: 1.0080× [0.9875, 1.0283].

### shape_m16_k16_n16__bfloat16

- S1: S1 products; [32, 512, 512]; b2; confirmed 0.2398 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9913× [0.9690, 1.0113].
  - other_buffers: 0.9906× [0.9727, 1.0118].
- S2: S2 outputs; [128, 512, 512]; b1; confirmed 0.2390 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0023× [0.9867, 1.0190].
  - other_buffers: 1.0078× [0.9942, 1.0215].

### shape_m64_k64_n64__float32

- S1: S1 products; [256, 512, 512]; b1; confirmed 0.2154 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0232× [1.0091, 1.0395].
  - other_buffers: 1.0181× [1.0000, 1.0407].
- S2: S2 outputs; [128, 512, 512]; b1; confirmed 0.2196 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9950× [0.9764, 1.0121].
  - other_buffers: 0.9980× [0.9815, 1.0151].

### shape_m64_k64_n64__bfloat16

- S1: S1 outputs; [128, 512, 512]; b1; confirmed 0.2188 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9991× [0.9845, 1.0145].
  - other_buffers: 0.9963× [0.9830, 1.0099].
- S2: S2 outputs; [32, 512, 512]; b1; confirmed 0.2177 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0003× [0.9747, 1.0268].
  - other_buffers: 0.9901× [0.9731, 1.0150].

### shape_m128_k128_n128__float32

- S1: S1 outputs; [32, 512, 512]; b1; confirmed 0.2293 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0077× [0.9516, 1.0850].
  - other_buffers: 0.9942× [0.9586, 1.0321].
- S2: S2 products; [256, 512, 512]; b2; confirmed 0.2278 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0024× [0.9800, 1.0224].
  - other_buffers: 1.0110× [0.9668, 1.0991].

### shape_m128_k128_n128__bfloat16

- S1: S1 outputs; [32, 512, 512]; b1; confirmed 0.2395 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0039× [0.9853, 1.0285].
  - other_buffers: 1.1147× [0.9709, 1.4940].
- S2: S2 products; [128, 512, 512]; b2; confirmed 0.2386 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9985× [0.9658, 1.0194].
  - other_buffers: 0.9997× [0.9823, 1.0178].

### shape_m256_k256_n256__float32

- S1: S1 outputs; [128, 512, 512]; b1; confirmed 0.2191 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0009× [0.9785, 1.0191].
  - other_buffers: 0.9922× [0.9686, 1.0140].
- S2: S2 products; [32, 512, 512]; b1; confirmed 0.2218 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9982× [0.9844, 1.0134].
  - other_buffers: 1.0025× [0.9854, 1.0188].

### shape_m256_k256_n256__bfloat16

- S1: S1 outputs; [128, 512, 512]; b1; confirmed 0.2227 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9962× [0.9757, 1.0142].
  - other_buffers: 0.9925× [0.9754, 1.0080].
- S2: S2 products; [32, 512, 512]; b1; confirmed 0.2258 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9910× [0.9727, 1.0077].
  - other_buffers: 1.0029× [0.9793, 1.0275].

### shape_m8_k2048_n2048__float32

- S1: S1 outputs; [128, 512, 512]; b2; confirmed 0.2316 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9815× [0.9429, 1.0044].
  - other_buffers: 1.0267× [0.9871, 1.0489].
- S2: S2 outputs; [128, 512, 512]; b2; confirmed 0.2290 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9983× [0.9862, 1.0106].
  - other_buffers: 1.0553× [1.0406, 1.0712].

### shape_m8_k2048_n2048__bfloat16

- S1: S1 products; [256, 512, 1024]; b2; confirmed 0.2354 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9996× [0.9838, 1.0185].
  - other_buffers: 1.0121× [0.9933, 1.0323].
- S2: S2 products; [256, 512, 2048]; b2; confirmed 0.2346 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0101× [0.9932, 1.0320].
  - other_buffers: 1.0296× [1.0162, 1.0441].

### shape_m2048_k8_n2048__float32

- S1: S1 outputs; [1024, 1024, 512]; b1; confirmed 0.2283 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9840× [0.9537, 1.0055].
  - other_buffers: 0.9866× [0.9517, 1.0121].
- S2: S2 outputs; [2048, 2048, 512]; b2; confirmed 0.2364 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0147× [0.9958, 1.0386].
  - other_buffers: 1.0106× [0.9880, 1.0414].

### shape_m2048_k8_n2048__bfloat16

- S1: S1 outputs; [2048, 1024, 512]; b2; confirmed 0.2505 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9914× [0.9749, 1.0059].
  - other_buffers: 0.9987× [0.9848, 1.0141].
- S2: S2 products; [1024, 1024, 512]; b2; confirmed 0.2538 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0039× [0.9851, 1.0281].
  - other_buffers: 0.9976× [0.9780, 1.0200].

### shape_m2048_k2048_n8__float32

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 0.2279 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9939× [0.9772, 1.0080].
  - other_buffers: 1.0090× [0.9869, 1.0367].
- S2: S2 outputs; [256, 512, 2048]; b2; confirmed 0.2460 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9768× [0.8877, 1.0330].
  - other_buffers: 0.9960× [0.9032, 1.0441].

### shape_m2048_k2048_n8__bfloat16

- S1: S1 outputs; [1024, 512, 512]; b2; confirmed 0.2330 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0078× [0.9884, 1.0326].
  - other_buffers: 1.0221× [1.0040, 1.0380].
- S2: S2 outputs; [512, 512, 2048]; b2; confirmed 0.2374 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9907× [0.9750, 1.0082].
  - other_buffers: 1.0200× [1.0046, 1.0341].

### shape_m384_k384_n384__float32

- S1: S1 products; [512, 512, 512]; b1; confirmed 0.2252 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0013× [0.9797, 1.0201].
  - other_buffers: 1.0138× [1.0002, 1.0282].
- S2: S2 products; [128, 512, 512]; b1; confirmed 0.2276 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0028× [0.9885, 1.0180].
  - other_buffers: 1.0257× [0.9845, 1.1170].

### shape_m384_k384_n384__bfloat16

- S1: S1 products; [512, 512, 512]; b2; confirmed 0.2440 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9819× [0.9642, 0.9978].
  - other_buffers: 0.9993× [0.9818, 1.0147].
- S2: S2 products; [128, 512, 512]; b1; confirmed 0.2429 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9865, 1.0167].
  - other_buffers: 0.9951× [0.9801, 1.0094].

### shape_m384_k1024_n256__float32

- S1: S1 outputs; [512, 512, 1024]; b1; confirmed 0.2331 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0106× [0.9894, 1.0401].
  - other_buffers: 1.0037× [0.9899, 1.0163].
- S2: S2 outputs; [512, 512, 1024]; b1; confirmed 0.2499 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9854× [0.8618, 1.1415].
  - other_buffers: 0.9567× [0.8634, 1.0104].

### shape_m384_k1024_n256__bfloat16

- S1: S1 outputs; [512, 512, 1024]; b1; confirmed 0.2344 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9973× [0.9820, 1.0129].
  - other_buffers: 0.9902× [0.9760, 1.0056].
- S2: S2 products; [128, 512, 1024]; b1; confirmed 0.2480 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9516× [0.8552, 1.0065].
  - other_buffers: 0.9649× [0.8728, 1.0333].

### shape_m512_k512_n512__float32

- S1: S1 outputs; [1024, 512, 512]; b2; confirmed 0.2410 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0088× [0.9923, 1.0287].
  - other_buffers: 0.9986× [0.9835, 1.0167].
- S2: S2 products; [512, 512, 512]; b1; confirmed 0.2386 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0076× [0.9790, 1.0495].
  - other_buffers: 0.9957× [0.9783, 1.0130].

### shape_m512_k512_n512__bfloat16

- S1: S1 products; [1024, 512, 512]; b2; confirmed 0.2464 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0096× [0.9790, 1.0325].
  - other_buffers: 1.0028× [0.9850, 1.0205].
- S2: S2 products; [512, 512, 512]; b1; confirmed 0.2523 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9699× [0.9405, 0.9973].
  - other_buffers: 0.9685× [0.9440, 0.9914].

### shape_m256_k1024_n768__float32

- S1: S1 outputs; [128, 512, 512]; b2; confirmed 0.2576 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0079× [0.9920, 1.0253].
  - other_buffers: 0.9995× [0.9888, 1.0104].
- S2: S2 outputs; [256, 512, 1024]; b1; confirmed 0.2583 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9894× [0.9745, 1.0034].
  - other_buffers: 0.9939× [0.9808, 1.0067].

### shape_m256_k1024_n768__bfloat16

- S1: S1 products; [32, 512, 1024]; b2; confirmed 0.2762 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9201× [0.7340, 1.0118].
  - other_buffers: 0.9175× [0.7367, 1.0074].
- S2: S2 products; [32, 512, 512]; b1; confirmed 0.2754 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9713× [0.8938, 1.0119].
  - other_buffers: 0.9670× [0.8889, 1.0074].

### shape_m512_k512_n768__float32

- S1: S1 outputs; [512, 512, 512]; b1; confirmed 0.2267 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9934× [0.9758, 1.0102].
  - other_buffers: 0.9878× [0.9720, 1.0022].
- S2: S2 outputs; [2048, 1024, 512]; b2; confirmed 0.2264 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0150× [0.9786, 1.0643].
  - other_buffers: 1.0013× [0.9834, 1.0203].

### shape_m512_k512_n768__bfloat16

- S1: S1 outputs; [4096, 1024, 512]; b2; confirmed 0.2438 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9945× [0.9754, 1.0122].
  - other_buffers: 1.0012× [0.9835, 1.0209].
- S2: S2 products; [1024, 2048, 512]; b1; confirmed 0.2444 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0006× [0.9863, 1.0162].
  - other_buffers: 0.9790× [0.9660, 0.9927].

### shape_m384_k1536_n512__float32

- S1: S1 outputs; [32, 512, 1536]; b2; confirmed 0.2407 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9359× [0.7697, 1.0160].
  - other_buffers: 0.9506× [0.7844, 1.0319].
- S2: S2 products; [512, 512, 512]; b2; confirmed 0.2241 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9978× [0.9792, 1.0221].
  - other_buffers: 0.9932× [0.9786, 1.0088].

### shape_m384_k1536_n512__bfloat16

- S1: S1 outputs; [128, 512, 512]; b1; confirmed 0.2369 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9925× [0.9774, 1.0066].
  - other_buffers: 0.9796× [0.9595, 1.0017].
- S2: S2 products; [512, 512, 512]; b2; confirmed 0.2316 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9985× [0.9804, 1.0152].
  - other_buffers: 1.0099× [0.9818, 1.0514].

### shape_m512_k2048_n384__float32

- S1: S1 products; [512, 512, 512]; b2; confirmed 0.2463 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0122× [0.9924, 1.0330].
  - other_buffers: 1.0049× [0.9751, 1.0306].
- S2: S2 products; [256, 512, 2048]; b1; confirmed 0.2467 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9975× [0.9836, 1.0100].
  - other_buffers: 1.0274× [1.0053, 1.0565].

### shape_m512_k2048_n384__bfloat16

- S1: S1 products; [512, 512, 2048]; b1; confirmed 0.2365 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0125× [0.9973, 1.0271].
  - other_buffers: 1.0077× [0.9851, 1.0268].
- S2: S2 outputs; [256, 512, 512]; b2; confirmed 0.2402 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0027× [0.9839, 1.0268].
  - other_buffers: 1.0034× [0.9874, 1.0219].

### shape_m512_k3072_n256__float32

- S1: S1 outputs; [128, 512, 512]; b2; confirmed 0.2396 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9988× [0.9832, 1.0174].
  - other_buffers: 1.0095× [0.9930, 1.0293].
- S2: S2 outputs; [256, 512, 3072]; b2; confirmed 0.2429 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9974× [0.9583, 1.0228].
  - other_buffers: 0.9893× [0.9593, 1.0138].

### shape_m512_k3072_n256__bfloat16

- S1: S1 products; [256, 512, 3072]; b2; confirmed 0.2383 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9898× [0.9759, 1.0021].
  - other_buffers: 0.9937× [0.9698, 1.0154].
- S2: S2 products; [512, 512, 512]; b1; confirmed 0.2410 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0115× [0.9897, 1.0549].
  - other_buffers: 1.0048× [0.9871, 1.0235].

### shape_m768_k768_n768__float32

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.2454 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0093× [0.9797, 1.0589].
  - other_buffers: 1.0036× [0.9898, 1.0162].
- S2: S2 outputs; [512, 512, 1024]; b2; confirmed 0.2422 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9822, 1.0194].
  - other_buffers: 1.0114× [0.9959, 1.0283].

### shape_m768_k768_n768__bfloat16

- S1: S1 outputs; [1024, 2048, 512]; b1; confirmed 0.2482 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9983× [0.9708, 1.0274].
  - other_buffers: 0.9987× [0.9770, 1.0226].
- S2: S2 outputs; [1024, 512, 1024]; b2; confirmed 0.2475 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9884× [0.9751, 1.0011].
  - other_buffers: 0.9923× [0.9750, 1.0086].

### shape_m512_k6144_n256__float32

- S1: S1 products; [512, 512, 3072]; b1; confirmed 0.2258 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0050× [0.9908, 1.0222].
  - other_buffers: 1.0001× [0.9801, 1.0244].
- S2: S2 outputs; [512, 512, 1024]; b1; confirmed 0.2315 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9850× [0.9665, 1.0012].
  - other_buffers: 0.9925× [0.9733, 1.0108].

### shape_m512_k6144_n256__bfloat16

- S1: S1 outputs; [512, 512, 1536]; b1; confirmed 0.2181 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9926× [0.9775, 1.0072].
  - other_buffers: 0.9960× [0.9705, 1.0217].
- S2: S2 products; [512, 512, 1024]; b1; confirmed 0.2201 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0001× [0.9774, 1.0244].
  - other_buffers: 0.9983× [0.9746, 1.0207].

### shape_m1536_k2048_n256__float32

- S1: S1 outputs; [512, 512, 512]; b2; confirmed 0.2413 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9977× [0.9883, 1.0084].
  - other_buffers: 1.0520× [1.0366, 1.0682].
- S2: S2 outputs; [512, 512, 2048]; b2; confirmed 0.2468 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9833× [0.9385, 1.0145].
  - other_buffers: 1.0050× [0.9604, 1.0398].

### shape_m1536_k2048_n256__bfloat16

- S1: S1 outputs; [512, 512, 512]; b2; confirmed 0.2420 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9921× [0.9750, 1.0114].
  - other_buffers: 1.0260× [1.0150, 1.0366].
- S2: S2 products; [256, 512, 2048]; b2; confirmed 0.2435 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0099× [0.9951, 1.0269].
  - other_buffers: 1.0762× [1.0265, 1.1970].

### shape_m1023_k1023_n1023__float32

- S1: S1 outputs; [512, 512, 512]; b1; confirmed 0.2381 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0124× [0.9883, 1.0548].
  - other_buffers: 0.9950× [0.9742, 1.0151].
- S2: S2 products; [1024, 2048, 1024]; b2; confirmed 0.2409 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1091× [1.0001, 1.3087].
  - other_buffers: 1.0381× [0.9971, 1.1132].

### shape_m1023_k1023_n1023__bfloat16

- S1: S1 products; [512, 512, 512]; b1; confirmed 0.2493 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0009× [0.9818, 1.0168].
  - other_buffers: 0.9948× [0.9684, 1.0295].
- S2: S2 outputs; [512, 512, 512]; b1; confirmed 0.2509 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9972× [0.9771, 1.0141].
  - other_buffers: 1.0083× [0.9904, 1.0363].

### shape_m64_k512_n32768__float32

- S1: S1 outputs; [128, 512, 512]; b2; confirmed 0.2913 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0049× [0.9956, 1.0148].
  - other_buffers: 1.1755× [1.1657, 1.1854].
- S2: S2 outputs; [128, 512, 512]; b2; confirmed 0.3023 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0004× [0.9877, 1.0143].
  - other_buffers: 1.2085× [1.1942, 1.2236].

### shape_m64_k512_n32768__bfloat16

- S1: S1 outputs; [128, 512, 512]; b2; confirmed 0.2858 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9964× [0.9817, 1.0116].
  - other_buffers: 1.1374× [1.1270, 1.1484].
- S2: S2 outputs; [128, 512, 512]; b2; confirmed 0.2909 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9981× [0.9835, 1.0155].
  - other_buffers: 1.1864× [1.1691, 1.2034].

### shape_m256_k2048_n2048__float32

- S1: S1 products; [256, 512, 2048]; b2; confirmed 0.2254 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9925× [0.9745, 1.0087].
  - other_buffers: 1.0215× [1.0088, 1.0365].
- S2: S2 products; [128, 512, 2048]; b2; confirmed 0.2320 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0077× [0.9809, 1.0394].
  - other_buffers: 1.0721× [1.0473, 1.0993].

### shape_m256_k2048_n2048__bfloat16

- S1: S1 outputs; [256, 512, 1024]; b2; confirmed 0.2311 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9999× [0.9863, 1.0157].
  - other_buffers: 1.0336× [1.0173, 1.0540].
- S2: S2 outputs; [256, 512, 512]; b2; confirmed 0.2342 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9998× [0.9839, 1.0198].
  - other_buffers: 1.0736× [1.0573, 1.0957].

### shape_m1024_k1024_n1024__float32

- S1: S1 outputs; [512, 512, 1024]; b2; confirmed 0.2350 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0035× [0.9902, 1.0193].
  - other_buffers: 1.0167× [1.0037, 1.0324].
- S2: S2 products; [2048, 1024, 1024]; b1; confirmed 0.2382 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0035× [0.9756, 1.0276].
  - other_buffers: 1.0062× [0.9838, 1.0278].

### shape_m1024_k1024_n1024__bfloat16

- S1: S1 outputs; [512, 512, 1024]; b2; confirmed 0.2367 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9931× [0.9825, 1.0036].
  - other_buffers: 1.0207× [0.9983, 1.0589].
- S2: S2 outputs; [512, 512, 1024]; b2; confirmed 0.2369 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0096× [0.9862, 1.0374].
  - other_buffers: 1.0209× [0.9969, 1.0524].

### shape_m2048_k256_n2048__float32

- S1: S1 products; [1024, 512, 512]; b1; confirmed 0.2319 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0022× [0.9919, 1.0133].
  - other_buffers: 0.9987× [0.9829, 1.0132].
- S2: S2 outputs; [1024, 2048, 512]; b2; confirmed 0.2402 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0029× [0.9899, 1.0160].
  - other_buffers: 1.0067× [0.9947, 1.0212].

### shape_m2048_k256_n2048__bfloat16

- S1: S1 products; [1024, 2048, 512]; b1; confirmed 0.2397 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9974× [0.9853, 1.0099].
  - other_buffers: 0.9907× [0.9736, 1.0074].
- S2: S2 outputs; [1024, 512, 512]; b1; confirmed 0.2455 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9977× [0.9781, 1.0283].
  - other_buffers: 0.9978× [0.9835, 1.0115].

### shape_m2048_k2048_n256__float32

- S1: S1 outputs; [1024, 512, 2048]; b1; confirmed 0.2419 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9833, 1.0218].
  - other_buffers: 0.9823× [0.9676, 0.9959].
- S2: S2 outputs; [1024, 512, 1024]; b2; confirmed 0.2430 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9833× [0.9634, 1.0019].
  - other_buffers: 1.0170× [1.0019, 1.0325].

### shape_m2048_k2048_n256__bfloat16

- S1: S1 outputs; [512, 512, 2048]; b2; confirmed 0.2367 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9979× [0.9832, 1.0116].
  - other_buffers: 1.0112× [0.9947, 1.0302].
- S2: S2 products; [512, 512, 1024]; b2; confirmed 0.2431 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9943× [0.9821, 1.0064].
  - other_buffers: 1.0283× [1.0167, 1.0402].

### shape_m32768_k512_n64__float32

- S1: S1 products; [1024, 512, 512]; b2; confirmed 0.3018 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0089× [0.9973, 1.0212].
  - other_buffers: 1.1199× [1.1022, 1.1350].
- S2: S2 products; [1024, 512, 512]; b2; confirmed 0.3089 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0027× [0.9920, 1.0133].
  - other_buffers: 1.1932× [1.1845, 1.2016].

### shape_m32768_k512_n64__bfloat16

- S1: S1 outputs; [1024, 512, 512]; b2; confirmed 0.2936 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9855× [0.9679, 0.9992].
  - other_buffers: 1.1378× [1.1162, 1.1551].
- S2: S2 products; [1024, 512, 512]; b2; confirmed 0.3063 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0057× [0.9934, 1.0182].
  - other_buffers: 1.1956× [1.1852, 1.2054].

### shape_m1025_k1025_n1025__float32

- S1: S1 products; [1024, 2048, 1536]; b1; confirmed 0.2654 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9968× [0.9774, 1.0140].
  - other_buffers: 0.9947× [0.9794, 1.0080].
- S2: S2 outputs; [1024, 512, 1536]; b2; confirmed 0.2703 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9900× [0.9779, 1.0022].
  - other_buffers: 0.9972× [0.9832, 1.0132].

### shape_m1025_k1025_n1025__bfloat16

- S1: S1 outputs; [1024, 512, 512]; b1; confirmed 0.2513 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9933× [0.9775, 1.0115].
  - other_buffers: 1.0098× [0.9940, 1.0270].
- S2: S2 outputs; [512, 512, 1536]; b1; confirmed 0.2515 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0110× [0.9911, 1.0483].
  - other_buffers: 1.0229× [0.9913, 1.0910].

### shape_m256_k6144_n768__float32

- S1: S1 outputs; [128, 512, 1536]; b2; confirmed 0.2585 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0025× [0.9892, 1.0175].
  - other_buffers: 1.0487× [1.0349, 1.0647].
- S2: S2 products; [256, 512, 6144]; b1; confirmed 0.2724 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9677× [0.8893, 1.0098].
  - other_buffers: 0.9666× [0.8911, 1.0054].

### shape_m256_k6144_n768__bfloat16

- S1: S1 products; [256, 512, 6144]; b2; confirmed 0.2470 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9978× [0.9845, 1.0113].
  - other_buffers: 0.9938× [0.9780, 1.0094].
- S2: S2 products; [256, 512, 1024]; b1; confirmed 0.2514 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0109× [0.9854, 1.0560].
  - other_buffers: 0.9998× [0.9775, 1.0238].

### shape_m1536_k1024_n768__float32

- S1: S1 outputs; [2048, 1024, 1024]; b2; confirmed 0.2450 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9731× [0.9455, 0.9983].
  - other_buffers: 0.9753× [0.9493, 0.9978].
- S2: S2 outputs; [512, 512, 1024]; b2; confirmed 0.2416 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9941× [0.9715, 1.0139].
  - other_buffers: 0.9909× [0.9765, 1.0062].

### shape_m1536_k1024_n768__bfloat16

- S1: S1 outputs; [512, 512, 1024]; b2; confirmed 0.2385 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9924× [0.9804, 1.0060].
  - other_buffers: 0.9978× [0.9858, 1.0146].
- S2: S2 outputs; [512, 512, 1024]; b2; confirmed 0.2400 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9939× [0.9782, 1.0081].
  - other_buffers: 0.9995× [0.9825, 1.0167].

### shape_m384_k3072_n2048__float32

- S1: S1 products; [512, 512, 1024]; b2; confirmed 0.2568 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9927× [0.9752, 1.0086].
  - other_buffers: 1.0454× [1.0213, 1.0648].
- S2: S2 products; [512, 512, 1024]; b2; confirmed 0.2618 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9971× [0.9869, 1.0072].
  - other_buffers: 1.0522× [1.0357, 1.0699].

### shape_m384_k3072_n2048__bfloat16

- S1: S1 products; [512, 512, 1536]; b2; confirmed 0.2540 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9982× [0.9686, 1.0330].
  - other_buffers: 1.0454× [1.0295, 1.0603].
- S2: S2 products; [512, 512, 1536]; b2; confirmed 0.2621 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9957× [0.9854, 1.0060].
  - other_buffers: 1.0569× [1.0441, 1.0739].

### shape_m384_k16384_n384__float32

- S1: S1 products; [128, 512, 16384]; b2; confirmed 0.2865 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0008× [0.9877, 1.0129].
  - other_buffers: 1.0019× [0.9921, 1.0120].
- S2: S2 outputs; [512, 512, 4096]; b2; confirmed 0.3039 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0001× [0.9844, 1.0173].
  - other_buffers: 1.0630× [1.0449, 1.0817].

### shape_m384_k16384_n384__bfloat16

- S1: S1 products; [128, 512, 16384]; b1; confirmed 0.2889 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0075× [0.9991, 1.0155].
  - other_buffers: 1.0163× [1.0002, 1.0339].
- S2: S2 outputs; [512, 512, 4096]; b2; confirmed 0.3104 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9947× [0.9859, 1.0039].
  - other_buffers: 1.0593× [1.0419, 1.0803].

### shape_m256_k2048_n6144__float32

- S1: S1 outputs; [256, 512, 2048]; b2; confirmed 0.2368 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9931× [0.9825, 1.0044].
  - other_buffers: 1.0825× [1.0709, 1.0948].
- S2: S2 outputs; [256, 512, 2048]; b2; confirmed 0.2436 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9963× [0.9842, 1.0088].
  - other_buffers: 1.1136× [1.0995, 1.1284].

### shape_m256_k2048_n6144__bfloat16

- S1: S1 outputs; [256, 512, 2048]; b2; confirmed 0.2422 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9979× [0.9859, 1.0088].
  - other_buffers: 1.0707× [1.0598, 1.0810].
- S2: S2 products; [256, 512, 2048]; b2; confirmed 0.2610 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9545× [0.8412, 1.0068].
  - other_buffers: 1.0611× [0.9394, 1.1160].

### shape_m4096_k1536_n512__float32

- S1: S1 outputs; [1024, 512, 1536]; b2; confirmed 0.2369 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9962× [0.9850, 1.0077].
  - other_buffers: 1.0307× [1.0197, 1.0420].
- S2: S2 outputs; [512, 512, 512]; b2; confirmed 0.2587 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9970× [0.9790, 1.0172].
  - other_buffers: 1.1031× [1.0863, 1.1196].

### shape_m4096_k1536_n512__bfloat16

- S1: S1 products; [1024, 512, 1536]; b2; confirmed 0.2407 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9982× [0.9806, 1.0119].
  - other_buffers: 1.0442× [1.0317, 1.0561].
- S2: S2 products; [2048, 1024, 1536]; b2; confirmed 0.2656 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9931× [0.9824, 1.0036].
  - other_buffers: 1.0046× [0.9903, 1.0178].

### shape_m32768_k256_n384__float32

- S1: S1 outputs; [1024, 512, 512]; b2; confirmed 0.4146 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0022× [0.9852, 1.0162].
  - other_buffers: 1.0916× [1.0789, 1.1060].
- S2: S2 products; [1024, 512, 512]; b2; confirmed 0.4203 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0108× [1.0019, 1.0220].
  - other_buffers: 1.1622× [1.1522, 1.1742].

### shape_m32768_k256_n384__bfloat16

- S1: S1 outputs; [512, 512, 512]; b2; confirmed 0.3762 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9943× [0.9848, 1.0036].
  - other_buffers: 1.1485× [1.1367, 1.1604].
- S2: S2 outputs; [1024, 512, 512]; b2; confirmed 0.3774 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9851× [0.9688, 0.9965].
  - other_buffers: 1.1533× [1.1299, 1.1715].

### shape_m384_k1536_n12288__float32

- S1: S1 outputs; [512, 512, 1536]; b2; confirmed 0.3044 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9982× [0.9890, 1.0084].
  - other_buffers: 1.1459× [1.1373, 1.1556].
- S2: S2 products; [512, 512, 1536]; b2; confirmed 0.3195 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0131× [0.9934, 1.0396].
  - other_buffers: 1.1902× [1.1765, 1.2062].

### shape_m384_k1536_n12288__bfloat16

- S1: S1 outputs; [512, 512, 1536]; b2; confirmed 0.2612 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0069× [0.9820, 1.0455].
  - other_buffers: 1.1284× [1.1049, 1.1500].
- S2: S2 outputs; [512, 512, 1536]; b2; confirmed 0.2842 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0051× [0.9919, 1.0186].
  - other_buffers: 1.1566× [1.1446, 1.1696].

### shape_m2048_k2048_n2048__float32

- S1: S1 products; [1024, 2048, 512]; b2; confirmed 0.2729 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9999× [0.9886, 1.0114].
  - other_buffers: 1.1142× [1.0541, 1.2745].
- S2: S2 outputs; [2048, 2048, 2048]; b2; confirmed 0.2836 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9918, 1.0120].
  - other_buffers: 0.9917× [0.9794, 1.0044].

### shape_m2048_k2048_n2048__bfloat16

- S1: S1 outputs; [2048, 1024, 512]; b2; confirmed 0.2530 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9858× [0.9714, 0.9982].
  - other_buffers: 1.0800× [1.0641, 1.1040].
- S2: S2 products; [1024, 1024, 2048]; b2; confirmed 0.2532 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9961× [0.9833, 1.0095].
  - other_buffers: 1.0571× [1.0404, 1.0725].

### shape_m256_k1536_n24576__float32

- S1: S1 outputs; [256, 512, 1536]; b2; confirmed 0.3082 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9961× [0.9839, 1.0079].
  - other_buffers: 1.2558× [1.2327, 1.2865].
- S2: S2 outputs; [256, 512, 1536]; b2; confirmed 0.3296 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0004× [0.9898, 1.0155].
  - other_buffers: 1.2844× [1.2727, 1.2956].

### shape_m256_k1536_n24576__bfloat16

- S1: S1 products; [256, 512, 1536]; b2; confirmed 0.2985 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9924× [0.9693, 1.0230].
  - other_buffers: 1.2152× [1.1893, 1.2332].
- S2: S2 products; [256, 512, 1536]; b2; confirmed 0.3179 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9919× [0.9800, 1.0037].
  - other_buffers: 1.2742× [1.2626, 1.2863].

### shape_m384_k6144_n4096__float32

- S1: S1 outputs; [512, 512, 6144]; b2; confirmed 0.2802 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9973× [0.9829, 1.0137].
  - other_buffers: 1.1069× [1.0918, 1.1232].
- S2: S2 products; [512, 512, 3072]; b2; confirmed 0.3222 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9943× [0.9785, 1.0073].
  - other_buffers: 1.1295× [1.1157, 1.1447].

### shape_m384_k6144_n4096__bfloat16

- S1: S1 outputs; [512, 512, 3072]; b2; confirmed 0.2872 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0000× [0.9801, 1.0183].
  - other_buffers: 1.1307× [1.1074, 1.1505].
- S2: S2 products; [512, 512, 1536]; b2; confirmed 0.3240 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9985× [0.9882, 1.0083].
  - other_buffers: 1.1810× [1.1649, 1.1963].

### shape_m256_k16384_n4096__float32

- S1: S1 products; [256, 512, 16384]; b2; confirmed 0.3380 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9963× [0.9874, 1.0043].
  - other_buffers: 1.1430× [1.1287, 1.1599].
- S2: S2 products; [256, 512, 8192]; b2; confirmed 0.3947 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9893× [0.9818, 0.9972].
  - other_buffers: 1.3268× [1.3112, 1.3409].

### shape_m256_k16384_n4096__bfloat16

- S1: S1 products; [256, 512, 16384]; b2; confirmed 0.3335 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9976× [0.9803, 1.0104].
  - other_buffers: 1.1488× [1.1293, 1.1642].
- S2: S2 products; [256, 512, 8192]; b2; confirmed 0.3885 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0018× [0.9907, 1.0136].
  - other_buffers: 1.3368× [1.3247, 1.3482].

### shape_m4096_k256_n16384__float32

- S1: S1 products; [4096, 1024, 512]; b2; confirmed 0.4421 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9999× [0.9902, 1.0096].
  - other_buffers: 1.0002× [0.9903, 1.0088].
- S2: S2 products; [2048, 1024, 512]; b2; confirmed 0.4606 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0075× [1.0012, 1.0136].
  - other_buffers: 1.1469× [1.1407, 1.1549].

### shape_m4096_k256_n16384__bfloat16

- S1: S1 outputs; [4096, 1024, 512]; b2; confirmed 0.3642 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0017× [0.9866, 1.0146].
  - other_buffers: 1.0558× [1.0334, 1.0710].
- S2: S2 outputs; [2048, 1024, 512]; b2; confirmed 0.4320 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0263× [1.0083, 1.0414].
  - other_buffers: 1.1842× [1.1635, 1.1965].

### shape_m16384_k256_n4096__float32

- S1: S1 outputs; [2048, 1024, 512]; b2; confirmed 0.4354 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9943× [0.9877, 1.0010].
  - other_buffers: 1.0288× [1.0225, 1.0350].
- S2: S2 outputs; [1024, 2048, 512]; b2; confirmed 0.4562 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0155× [1.0082, 1.0225].
  - other_buffers: 1.0497× [1.0432, 1.0564].

### shape_m16384_k256_n4096__bfloat16

- S1: S1 products; [1024, 2048, 512]; b2; confirmed 0.3635 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0001× [0.9874, 1.0149].
  - other_buffers: 1.0990× [1.0887, 1.1104].
- S2: S2 outputs; [4096, 1024, 512]; b2; confirmed 0.4284 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0242× [1.0144, 1.0345].
  - other_buffers: 1.0442× [1.0377, 1.0512].

### shape_m256_k24576_n3072__float32

- S1: S1 outputs; [256, 512, 24576]; b2; confirmed 0.3514 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0074× [0.9960, 1.0188].
  - other_buffers: 1.1548× [1.1424, 1.1674].
- S2: S2 outputs; [256, 512, 6144]; b2; confirmed 0.4120 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9881× [0.9804, 0.9958].
  - other_buffers: 1.3751× [1.3615, 1.3882].

### shape_m256_k24576_n3072__bfloat16

- S1: S1 outputs; [256, 512, 24576]; b2; confirmed 0.3386 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0000× [0.9916, 1.0090].
  - other_buffers: 1.1512× [1.1410, 1.1618].
- S2: S2 products; [256, 512, 6144]; b2; confirmed 0.3961 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9996× [0.9919, 1.0073].
  - other_buffers: 1.3927× [1.3831, 1.4028].

### shape_m256_k49152_n1536__float32

- S1: S1 outputs; [256, 512, 12288]; b2; confirmed 0.3891 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9980× [0.9888, 1.0087].
  - other_buffers: 1.1694× [1.1560, 1.1873].
- S2: S2 products; [256, 512, 12288]; b2; confirmed 0.4135 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9930, 1.0107].
  - other_buffers: 1.3444× [1.3284, 1.3619].

### shape_m256_k49152_n1536__bfloat16

- S1: S1 outputs; [256, 512, 12288]; b2; confirmed 0.3855 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0008× [0.9920, 1.0106].
  - other_buffers: 1.1748× [1.1664, 1.1840].
- S2: S2 products; [256, 512, 12288]; b2; confirmed 0.4110 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0044× [0.9961, 1.0157].
  - other_buffers: 1.3433× [1.3277, 1.3578].

### shape_m384_k384_n131072__float32

- S1: S1 products; [512, 512, 512]; b2; confirmed 1.0040 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0072× [1.0041, 1.0110].
  - other_buffers: 1.2187× [1.2137, 1.2237].
- S2: S2 products; [512, 512, 512]; b2; confirmed 1.0477 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0077× [1.0026, 1.0117].
  - other_buffers: 1.2879× [1.2829, 1.2922].

### shape_m384_k384_n131072__bfloat16

- S1: S1 outputs; [512, 512, 512]; b2; confirmed 0.7956 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9978× [0.9935, 1.0020].
  - other_buffers: 1.3055× [1.2996, 1.3120].
- S2: S2 outputs; [512, 512, 512]; b2; confirmed 0.8598 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9979× [0.9912, 1.0063].
  - other_buffers: 1.3523× [1.3435, 1.3630].

### shape_m1536_k8192_n1536__float32

- S1: S1 products; [512, 512, 8192]; b2; confirmed 0.3145 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0038× [0.9948, 1.0128].
  - other_buffers: 1.1487× [1.1404, 1.1575].
- S2: S2 outputs; [512, 512, 4096]; b2; confirmed 0.3599 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0162× [1.0017, 1.0339].
  - other_buffers: 1.2967× [1.2883, 1.3048].

### shape_m1536_k8192_n1536__bfloat16

- S1: S1 products; [512, 512, 8192]; b2; confirmed 0.3177 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9962× [0.9866, 1.0047].
  - other_buffers: 1.1453× [1.1326, 1.1579].
- S2: S2 outputs; [512, 512, 2048]; b2; confirmed 0.3659 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0074× [0.9995, 1.0143].
  - other_buffers: 1.3216× [1.3129, 1.3316].

### shape_m6144_k2048_n1536__float32

- S1: S1 outputs; [1024, 512, 2048]; b2; confirmed 0.2968 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0029× [0.9754, 1.0282].
  - other_buffers: 1.1613× [1.1447, 1.1764].
- S2: S2 outputs; [1024, 512, 2048]; b2; confirmed 0.3167 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9999× [0.9924, 1.0082].
  - other_buffers: 1.2235× [1.2139, 1.2322].

### shape_m6144_k2048_n1536__bfloat16

- S1: S1 products; [1024, 512, 2048]; b2; confirmed 0.2913 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0006× [0.9911, 1.0097].
  - other_buffers: 1.1632× [1.1533, 1.1725].
- S2: S2 products; [1024, 512, 2048]; b2; confirmed 0.3198 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9915× [0.9792, 1.0039].
  - other_buffers: 1.1936× [1.1740, 1.2095].

### shape_m768_k3072_n12288__float32

- S1: S1 products; [1024, 512, 3072]; b2; confirmed 0.4114 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9798× [0.9188, 1.0081].
  - other_buffers: 1.2151× [1.1362, 1.2496].
- S2: S2 outputs; [1024, 2048, 3072]; b2; confirmed 0.4352 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0025× [0.9963, 1.0094].
  - other_buffers: 1.1779× [1.1677, 1.1940].

### shape_m768_k3072_n12288__bfloat16

- S1: S1 products; [1024, 512, 3072]; b2; confirmed 0.3512 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9981× [0.9885, 1.0078].
  - other_buffers: 1.2531× [1.2420, 1.2656].
- S2: S2 outputs; [1024, 1024, 3072]; b2; confirmed 0.3956 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9591× [0.8447, 1.0106].
  - other_buffers: 1.1453× [1.0092, 1.2122].

### shape_m768_k12288_n3072__float32

- S1: S1 outputs; [1024, 512, 12288]; b2; confirmed 0.4102 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9949× [0.9803, 1.0099].
  - other_buffers: 1.1190× [1.1035, 1.1342].
- S2: S2 products; [1024, 1024, 3072]; b2; confirmed 0.4290 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0139× [0.9899, 1.0390].
  - other_buffers: 1.2276× [1.2011, 1.2508].

### shape_m768_k12288_n3072__bfloat16

- S1: S1 outputs; [1024, 1024, 6144]; b2; confirmed 0.4200 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0039× [0.9894, 1.0201].
  - other_buffers: 1.1828× [1.1566, 1.2037].
- S2: S2 products; [1024, 1024, 1024]; b2; confirmed 0.4315 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0121× [0.9973, 1.0272].
  - other_buffers: 1.2874× [1.2711, 1.3056].

### shape_m3072_k768_n12288__float32

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 0.6063 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9487× [0.8166, 1.0462].
  - other_buffers: 1.1795× [1.0504, 1.2839].
- S2: S2 outputs; [1024, 1024, 1024]; b2; confirmed 0.5769 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9808× [0.9039, 1.0657].
  - other_buffers: 1.2592× [1.1766, 1.3523].

### shape_m3072_k768_n12288__bfloat16

- S1: S1 outputs; [1024, 2048, 1024]; b2; confirmed 0.4234 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9629× [0.9281, 0.9891].
  - other_buffers: 1.2226× [1.1851, 1.2505].
- S2: S2 outputs; [1024, 1024, 1024]; b2; confirmed 0.4368 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9989× [0.9709, 1.0267].
  - other_buffers: 1.2863× [1.2586, 1.3120].

### shape_m3072_k12288_n768__float32

- S1: S1 products; [1024, 1024, 3072]; b2; confirmed 0.4287 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0049× [0.9888, 1.0197].
  - other_buffers: 1.2064× [1.1789, 1.2320].
- S2: S2 outputs; [1024, 1024, 6144]; b2; confirmed 0.4515 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9966× [0.9769, 1.0140].
  - other_buffers: 1.1876× [1.1722, 1.2035].

### shape_m3072_k12288_n768__bfloat16

- S1: S1 outputs; [1024, 1024, 6144]; b2; confirmed 0.3965 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0019× [0.9935, 1.0101].
  - other_buffers: 1.1999× [1.1847, 1.2280].
- S2: S2 products; [1024, 1024, 3072]; b1; confirmed 0.4966 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0031× [0.9972, 1.0085].
  - other_buffers: 0.8083× [0.8030, 0.8138].

### shape_m12288_k768_n3072__float32

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.3821 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0092× [0.9959, 1.0199].
  - other_buffers: 1.0542× [1.0407, 1.0669].
- S2: S2 products; [4096, 1024, 1024]; b2; confirmed 0.4249 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9607× [0.8414, 1.0125].
  - other_buffers: 0.9918× [0.8686, 1.0452].

### shape_m12288_k768_n3072__bfloat16

- S1: S1 outputs; [2048, 1024, 1024]; b2; confirmed 0.3793 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9965× [0.9887, 1.0066].
  - other_buffers: 1.0561× [1.0469, 1.0656].
- S2: S2 outputs; [1024, 1024, 1024]; b2; confirmed 0.4084 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9970× [0.9867, 1.0069].
  - other_buffers: 1.0841× [1.0729, 1.0937].

### shape_m12288_k3072_n768__float32

- S1: S1 outputs; [1024, 1024, 3072]; b2; confirmed 0.4087 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0046× [0.9912, 1.0195].
  - other_buffers: 1.2122× [1.1987, 1.2280].
- S2: S2 products; [2048, 1024, 3072]; b1; confirmed 0.4995 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0060× [0.9956, 1.0169].
  - other_buffers: 0.8522× [0.8428, 0.8608].

### shape_m12288_k3072_n768__bfloat16

- S1: S1 products; [1024, 1024, 3072]; b2; confirmed 0.3690 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9904× [0.9750, 1.0019].
  - other_buffers: 1.1855× [1.1633, 1.2044].
- S2: S2 outputs; [2048, 1024, 3072]; b2; confirmed 0.3849 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9947× [0.9829, 1.0071].
  - other_buffers: 1.1585× [1.1432, 1.1753].

### shape_m2047_k4096_n4096__float32

- S1: S1 products; [2048, 1024, 4096]; b2; confirmed 0.3577 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0022× [0.9887, 1.0172].
  - other_buffers: 1.1134× [1.0949, 1.1361].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.3691 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9903× [0.9754, 1.0033].
  - other_buffers: 1.0929× [1.0724, 1.1074].

### shape_m2047_k4096_n4096__bfloat16

- S1: S1 outputs; [2048, 1024, 4096]; b2; confirmed 0.3581 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9930× [0.9793, 1.0073].
  - other_buffers: 1.0758× [1.0656, 1.0874].
- S2: S2 outputs; [2048, 1024, 2048]; b2; confirmed 0.3643 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9960× [0.9864, 1.0047].
  - other_buffers: 1.1989× [1.1779, 1.2258].

### shape_m2048_k8191_n2048__float32

- S1: S1 outputs; [1024, 512, 8192]; b2; confirmed 0.4369 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9982× [0.9900, 1.0082].
  - other_buffers: 1.1276× [1.1162, 1.1399].
- S2: S2 products; [2048, 1024, 8192]; b2; confirmed 0.4632 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9984× [0.9896, 1.0077].
  - other_buffers: 1.0373× [1.0297, 1.0457].

### shape_m2048_k8191_n2048__bfloat16

- S1: S1 outputs; [2048, 2048, 8192]; b1; confirmed 0.4694 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9962× [0.9882, 1.0041].
  - other_buffers: 0.9987× [0.9912, 1.0069].
- S2: S2 products; [1024, 2048, 512]; b2; confirmed 0.5138 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0466× [1.0391, 1.0538].
  - other_buffers: 1.1782× [1.1690, 1.1865].

### shape_m512_k4096_n16384__float32

- S1: S1 outputs; [512, 512, 4096]; b2; confirmed 0.3468 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0226× [0.9905, 1.0898].
  - other_buffers: 1.3129× [1.3006, 1.3259].
- S2: S2 products; [512, 512, 4096]; b2; confirmed 0.4275 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0047× [0.9922, 1.0188].
  - other_buffers: 1.3141× [1.2978, 1.3294].

### shape_m512_k4096_n16384__bfloat16

- S1: S1 outputs; [512, 512, 4096]; b2; confirmed 0.3452 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0008× [0.9908, 1.0115].
  - other_buffers: 1.3156× [1.2938, 1.3482].
- S2: S2 outputs; [512, 512, 4096]; b2; confirmed 0.4335 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0106× [0.9897, 1.0520].
  - other_buffers: 1.2923× [1.2706, 1.3305].

### shape_m512_k16384_n4096__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 0.3550 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0021× [0.9919, 1.0142].
  - other_buffers: 1.2097× [1.1975, 1.2211].
- S2: S2 products; [512, 512, 16384]; b2; confirmed 0.4429 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9948× [0.9849, 1.0042].
  - other_buffers: 1.1930× [1.1792, 1.2067].

### shape_m512_k16384_n4096__bfloat16

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 0.3568 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0058× [0.9931, 1.0198].
  - other_buffers: 1.2161× [1.2018, 1.2332].
- S2: S2 outputs; [512, 512, 16384]; b2; confirmed 0.4474 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9989× [0.9923, 1.0067].
  - other_buffers: 1.1955× [1.1845, 1.2095].

### shape_m2048_k1024_n16384__float32

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.3673 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0050× [0.9930, 1.0169].
  - other_buffers: 1.0924× [1.0791, 1.1074].
- S2: S2 products; [2048, 1024, 1024]; b2; confirmed 0.3726 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0060× [0.9927, 1.0210].
  - other_buffers: 1.1608× [1.1452, 1.1813].

### shape_m2048_k1024_n16384__bfloat16

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.3195 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9989× [0.9888, 1.0109].
  - other_buffers: 1.1984× [1.1859, 1.2109].
- S2: S2 outputs; [2048, 2048, 1024]; b2; confirmed 0.3460 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0133× [1.0053, 1.0208].
  - other_buffers: 1.1356× [1.1240, 1.1472].

### shape_m4096_k512_n16384__float32

- S1: S1 outputs; [4096, 1024, 512]; b1; confirmed 0.4200 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9997× [0.9833, 1.0102].
  - other_buffers: 1.0052× [0.9868, 1.0177].
- S2: S2 outputs; [2048, 2048, 512]; b2; confirmed 0.4409 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0080× [0.9992, 1.0155].
  - other_buffers: 1.1030× [1.0952, 1.1106].

### shape_m4096_k512_n16384__bfloat16

- S1: S1 outputs; [4096, 1024, 512]; b2; confirmed 0.3331 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9936× [0.9804, 1.0057].
  - other_buffers: 1.0720× [1.0609, 1.0823].
- S2: S2 outputs; [4096, 1024, 512]; b2; confirmed 0.4055 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0232× [1.0148, 1.0319].
  - other_buffers: 1.0977× [1.0793, 1.1163].

### shape_m4096_k16384_n512__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 0.3512 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9909× [0.9684, 1.0093].
  - other_buffers: 1.2331× [1.1830, 1.3213].
- S2: S2 products; [1024, 512, 4096]; b2; confirmed 0.3991 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0110× [1.0011, 1.0208].
  - other_buffers: 1.3323× [1.3135, 1.3523].

### shape_m4096_k16384_n512__bfloat16

- S1: S1 products; [512, 512, 16384]; b2; confirmed 0.3502 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0034× [0.9890, 1.0175].
  - other_buffers: 1.2060× [1.1840, 1.2271].
- S2: S2 products; [1024, 512, 4096]; b2; confirmed 0.3994 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0013× [0.9917, 1.0104].
  - other_buffers: 1.3358× [1.3233, 1.3484].

### shape_m16384_k512_n4096__float32

- S1: S1 outputs; [4096, 1024, 512]; b2; confirmed 0.4447 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0007× [0.9898, 1.0106].
  - other_buffers: 1.0077× [0.9963, 1.0185].
- S2: S2 products; [4096, 1024, 512]; b2; confirmed 0.4617 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0090× [1.0008, 1.0174].
  - other_buffers: 1.0929× [1.0837, 1.1016].

### shape_m16384_k512_n4096__bfloat16

- S1: S1 outputs; [4096, 1024, 512]; b2; confirmed 0.3522 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0030× [0.9922, 1.0167].
  - other_buffers: 1.0951× [1.0845, 1.1062].
- S2: S2 outputs; [4096, 1024, 512]; b2; confirmed 0.4166 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0201× [1.0110, 1.0284].
  - other_buffers: 1.1345× [1.1237, 1.1468].

### shape_m16384_k4096_n512__float32

- S1: S1 outputs; [512, 512, 4096]; b2; confirmed 0.3631 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9771× [0.9170, 1.0046].
  - other_buffers: 1.2704× [1.1894, 1.3079].
- S2: S2 products; [1024, 512, 4096]; b2; confirmed 0.3959 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0045× [0.9945, 1.0139].
  - other_buffers: 1.2921× [1.2832, 1.3015].

### shape_m16384_k4096_n512__bfloat16

- S1: S1 products; [512, 512, 4096]; b2; confirmed 0.3507 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0122× [0.9962, 1.0368].
  - other_buffers: 1.2839× [1.2667, 1.2979].
- S2: S2 products; [1024, 512, 4096]; b2; confirmed 0.4001 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0006× [0.9926, 1.0085].
  - other_buffers: 1.2623× [1.2520, 1.2714].

### shape_m2048_k8193_n2048__float32

- S1: S1 outputs; [2048, 2048, 512]; b2; confirmed 0.4495 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9777× [0.9654, 0.9884].
  - other_buffers: 1.1141× [1.1004, 1.1258].
- S2: S2 products; [2048, 1024, 8704]; b2; confirmed 0.4880 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0177× [0.9983, 1.0528].
  - other_buffers: 1.0472× [1.0376, 1.0567].

### shape_m2048_k8193_n2048__bfloat16

- S1: S1 products; [2048, 2048, 512]; b2; confirmed 0.4364 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0703× [1.0352, 1.1575].
  - other_buffers: 1.1334× [1.1256, 1.1424].
- S2: S2 outputs; [1024, 1024, 8704]; b2; confirmed 0.4770 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0020× [0.9933, 1.0134].
  - other_buffers: 1.1091× [1.1004, 1.1185].

### shape_m2049_k4096_n4096__float32

- S1: S1 outputs; [1024, 512, 4096]; b2; confirmed 0.4726 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9918× [0.9749, 1.0040].
  - other_buffers: 1.2388× [1.2209, 1.2518].
- S2: S2 products; [1024, 1024, 4096]; b2; confirmed 0.4955 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0082× [0.9995, 1.0175].
  - other_buffers: 1.2036× [1.1931, 1.2130].

### shape_m2049_k4096_n4096__bfloat16

- S1: S1 outputs; [1024, 512, 4096]; b2; confirmed 0.4173 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9998× [0.9911, 1.0089].
  - other_buffers: 1.2499× [1.2363, 1.2678].
- S2: S2 products; [1024, 1024, 4096]; b2; confirmed 0.4442 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0156× [0.9952, 1.0637].
  - other_buffers: 1.2095× [1.2011, 1.2180].

### shape_m768_k8192_n6144__float32

- S1: S1 outputs; [1024, 512, 8192]; b2; confirmed 0.4135 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0037× [0.9928, 1.0152].
  - other_buffers: 1.2199× [1.2021, 1.2355].
- S2: S2 outputs; [1024, 1024, 8192]; b2; confirmed 0.4570 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9923× [0.9855, 0.9986].
  - other_buffers: 1.1541× [1.1448, 1.1626].

### shape_m768_k8192_n6144__bfloat16

- S1: S1 outputs; [1024, 512, 8192]; b2; confirmed 0.3999 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0029× [0.9933, 1.0139].
  - other_buffers: 1.1834× [1.1735, 1.1936].
- S2: S2 products; [1024, 1024, 4096]; b2; confirmed 0.4381 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0043× [0.9907, 1.0153].
  - other_buffers: 1.2877× [1.2716, 1.2990].

### shape_m1536_k384_n65536__float32

- S1: S1 outputs; [512, 512, 512]; b2; confirmed 0.8057 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9906× [0.9842, 0.9972].
  - other_buffers: 1.4523× [1.4453, 1.4595].
- S2: S2 products; [512, 512, 512]; b2; confirmed 0.8657 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0172× [1.0111, 1.0240].
  - other_buffers: 1.5512× [1.5443, 1.5572].

### shape_m1536_k384_n65536__bfloat16

- S1: S1 outputs; [512, 512, 512]; b2; confirmed 0.7062 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9939× [0.9878, 0.9995].
  - other_buffers: 1.5302× [1.5180, 1.5418].
- S2: S2 products; [512, 512, 512]; b2; confirmed 0.7928 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9979× [0.9941, 1.0016].
  - other_buffers: 1.5862× [1.5771, 1.5978].

### shape_m1536_k16384_n1536__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 0.3957 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9997× [0.9856, 1.0131].
  - other_buffers: 1.2197× [1.2062, 1.2354].
- S2: S2 outputs; [512, 512, 16384]; b2; confirmed 0.4761 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0003× [0.9920, 1.0106].
  - other_buffers: 1.2413× [1.2330, 1.2492].

### shape_m1536_k16384_n1536__bfloat16

- S1: S1 products; [512, 512, 4096]; b2; confirmed 0.4447 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9623× [0.8638, 1.0097].
  - other_buffers: 1.2724× [1.1369, 1.3464].
- S2: S2 products; [1024, 512, 8192]; b2; confirmed 0.5597 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9966× [0.9835, 1.0046].
  - other_buffers: 1.3349× [1.3102, 1.3610].

### shape_m12288_k1536_n2048__float32

- S1: S1 outputs; [1024, 2048, 1536]; b2; confirmed 0.3461 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0277× [0.9792, 1.1485].
  - other_buffers: 1.1857× [1.1721, 1.2002].
- S2: S2 products; [2048, 2048, 1536]; b2; confirmed 0.3868 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9886× [0.9777, 1.0011].
  - other_buffers: 1.1298× [1.1194, 1.1405].

### shape_m12288_k1536_n2048__bfloat16

- S1: S1 outputs; [1024, 2048, 1536]; b2; confirmed 0.3540 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9763× [0.9138, 1.0060].
  - other_buffers: 1.1539× [1.0818, 1.1907].
- S2: S2 outputs; [2048, 1024, 1536]; b2; confirmed 0.3786 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0075× [0.9985, 1.0174].
  - other_buffers: 1.2342× [1.2238, 1.2453].

### shape_m32768_k1024_n1536__float32

- S1: S1 outputs; [1024, 512, 1024]; b2; confirmed 0.5427 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9947× [0.9890, 1.0006].
  - other_buffers: 1.3298× [1.3238, 1.3362].
- S2: S2 products; [1024, 512, 1024]; b2; confirmed 0.5696 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0128× [1.0027, 1.0241].
  - other_buffers: 1.4646× [1.4493, 1.4795].

### shape_m32768_k1024_n1536__bfloat16

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 0.4504 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9972× [0.9911, 1.0031].
  - other_buffers: 1.4012× [1.3917, 1.4101].
- S2: S2 outputs; [1024, 512, 1024]; b2; confirmed 0.5211 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9934× [0.9497, 1.0142].
  - other_buffers: 1.4430× [1.3831, 1.4699].

### shape_m49152_k512_n2048__float32

- S1: S1 products; [2048, 2048, 512]; b1; confirmed 0.5403 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0039× [0.9964, 1.0127].
  - other_buffers: 1.0044× [0.9953, 1.0138].
- S2: S2 outputs; [2048, 2048, 512]; b2; confirmed 0.5498 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0014× [0.9950, 1.0077].
  - other_buffers: 1.1315× [1.1226, 1.1419].

### shape_m49152_k512_n2048__bfloat16

- S1: S1 outputs; [1024, 2048, 512]; b2; confirmed 0.4128 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9996× [0.9718, 1.0159].
  - other_buffers: 1.2223× [1.1956, 1.2402].
- S2: S2 outputs; [2048, 2048, 512]; b2; confirmed 0.5093 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0292× [1.0183, 1.0477].
  - other_buffers: 1.1915× [1.1855, 1.1983].

### shape_m49152_k4096_n256__float32

- S1: S1 outputs; [1024, 512, 4096]; b2; confirmed 0.6732 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0188× [0.9878, 1.0949].
  - other_buffers: 1.3750× [1.3588, 1.3851].
- S2: S2 products; [1024, 512, 4096]; b2; confirmed 0.7879 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9951× [0.9382, 1.0238].
  - other_buffers: 1.4447× [1.3680, 1.4758].

### shape_m49152_k4096_n256__bfloat16

- S1: S1 outputs; [1024, 512, 4096]; b2; confirmed 0.5901 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9967× [0.9802, 1.0111].
  - other_buffers: 1.4401× [1.4184, 1.4617].
- S2: S2 products; [1024, 512, 4096]; b2; confirmed 0.7427 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9936× [0.9850, 1.0007].
  - other_buffers: 1.4346× [1.4154, 1.4567].

### shape_m98304_k1024_n512__float32

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 0.5142 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0001× [0.9937, 1.0058].
  - other_buffers: 1.4001× [1.3917, 1.4095].
- S2: S2 products; [1024, 512, 1024]; b2; confirmed 0.5427 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0118× [1.0069, 1.0167].
  - other_buffers: 1.5524× [1.5424, 1.5627].

### shape_m98304_k1024_n512__bfloat16

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 0.4625 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9970× [0.9882, 1.0050].
  - other_buffers: 1.4202× [1.4026, 1.4413].
- S2: S2 outputs; [1024, 512, 1024]; b2; confirmed 0.5118 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0052× [0.9980, 1.0132].
  - other_buffers: 1.5290× [1.4986, 1.5863].

### shape_m4095_k4095_n4095__float32

- S1: S1 outputs; [2048, 1024, 4096]; b2; confirmed 0.5152 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0041× [0.9911, 1.0265].
  - other_buffers: 1.1770× [1.1690, 1.1856].
- S2: S2 outputs; [2048, 1024, 4096]; b2; confirmed 0.5262 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0016× [0.9878, 1.0136].
  - other_buffers: 1.1997× [1.1643, 1.2807].

### shape_m4095_k4095_n4095__bfloat16

- S1: S1 outputs; [2048, 1024, 4096]; b2; confirmed 0.5028 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0019× [0.9940, 1.0102].
  - other_buffers: 1.1470× [1.1338, 1.1609].
- S2: S2 outputs; [2048, 1024, 4096]; b2; confirmed 0.5245 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9855× [0.9490, 1.0033].
  - other_buffers: 1.1311× [1.0887, 1.1519].

### shape_m2048_k4096_n8191__float32

- S1: S1 products; [2048, 1024, 4096]; b2; confirmed 0.5126 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0016× [0.9894, 1.0204].
  - other_buffers: 1.1734× [1.1641, 1.1814].
- S2: S2 outputs; [2048, 2048, 4096]; b2; confirmed 0.5647 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9790× [0.8991, 1.0142].
  - other_buffers: 1.0945× [1.0086, 1.1314].

### shape_m2048_k4096_n8191__bfloat16

- S1: S1 outputs; [1024, 512, 4096]; b2; confirmed 0.4917 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0048× [0.9966, 1.0124].
  - other_buffers: 1.2820× [1.2680, 1.3105].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.5082 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9930× [0.9812, 1.0011].
  - other_buffers: 1.1344× [1.1235, 1.1446].

### shape_m2048_k2048_n16384__float32

- S1: S1 products; [2048, 1024, 2048]; b2; confirmed 0.4061 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0132× [1.0025, 1.0221].
  - other_buffers: 1.2645× [1.2438, 1.2831].
- S2: S2 outputs; [1024, 1024, 2048]; b2; confirmed 0.4683 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0022× [0.9902, 1.0188].
  - other_buffers: 1.4343× [1.4240, 1.4445].

### shape_m2048_k2048_n16384__bfloat16

- S1: S1 outputs; [1024, 512, 2048]; b2; confirmed 0.4427 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9881× [0.9761, 1.0005].
  - other_buffers: 1.3938× [1.3805, 1.4065].
- S2: S2 products; [2048, 1024, 2048]; b2; confirmed 0.4432 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9982× [0.9803, 1.0161].
  - other_buffers: 1.2233× [1.2038, 1.2409].

### shape_m2048_k16384_n2048__float32

- S1: S1 products; [2048, 1024, 4096]; b2; confirmed 0.4251 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0317× [0.9874, 1.1319].
  - other_buffers: 1.2825× [1.2578, 1.2972].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.4331 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0589× [1.0140, 1.1742].
  - other_buffers: 1.2815× [1.2656, 1.2988].

### shape_m2048_k16384_n2048__bfloat16

- S1: S1 outputs; [2048, 1024, 4096]; b2; confirmed 0.4533 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9401× [0.8422, 1.0009].
  - other_buffers: 1.2163× [1.0897, 1.3077].
- S2: S2 outputs; [2048, 1024, 4096]; b2; confirmed 0.4400 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9852× [0.9738, 0.9962].
  - other_buffers: 1.2670× [1.2501, 1.2806].

### shape_m4096_k4096_n4096__float32

- S1: S1 products; [2048, 1024, 4096]; b2; confirmed 0.4397 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9639× [0.8696, 1.0054].
  - other_buffers: 1.1742× [1.0530, 1.2344].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.4408 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9864× [0.9618, 1.0058].
  - other_buffers: 1.1938× [1.1627, 1.2243].

### shape_m4096_k4096_n4096__bfloat16

- S1: S1 outputs; [2048, 2048, 1024]; b2; confirmed 0.4260 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9811× [0.9003, 1.0165].
  - other_buffers: 1.2652× [1.1727, 1.3405].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.4227 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9926× [0.9829, 1.0015].
  - other_buffers: 1.1851× [1.1704, 1.1998].

### shape_m16384_k2048_n2048__float32

- S1: S1 products; [1024, 2048, 2048]; b2; confirmed 0.4063 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0207× [0.9994, 1.0508].
  - other_buffers: 1.2727× [1.2509, 1.2903].
- S2: S2 outputs; [2048, 2048, 2048]; b2; confirmed 0.4313 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0107× [1.0037, 1.0168].
  - other_buffers: 1.2169× [1.2049, 1.2303].

### shape_m16384_k2048_n2048__bfloat16

- S1: S1 products; [2048, 2048, 2048]; b2; confirmed 0.4064 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9663× [0.9072, 1.0053].
  - other_buffers: 1.1873× [1.1126, 1.2405].
- S2: S2 outputs; [4096, 1024, 2048]; b2; confirmed 0.4152 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9998× [0.9890, 1.0104].
  - other_buffers: 1.2165× [1.2021, 1.2294].

### shape_m2048_k4096_n8193__float32

- S1: S1 products; [1024, 512, 4096]; b2; confirmed 0.6741 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9928× [0.9593, 1.0102].
  - other_buffers: 1.2412× [1.2052, 1.2610].
- S2: S2 outputs; [2048, 1024, 4096]; b2; confirmed 0.7084 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9770× [0.9038, 1.0094].
  - other_buffers: 1.1224× [1.0404, 1.1577].

### shape_m2048_k4096_n8193__bfloat16

- S1: S1 outputs; [1024, 512, 4096]; b2; confirmed 0.6045 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0003× [0.9953, 1.0054].
  - other_buffers: 1.2445× [1.2377, 1.2527].
- S2: S2 outputs; [2048, 1024, 4096]; b2; confirmed 0.6264 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0043× [0.9957, 1.0121].
  - other_buffers: 1.1250× [1.1171, 1.1312].

### shape_m4097_k4097_n4097__float32

- S1: S1 outputs; [1024, 512, 4608]; b2; confirmed 0.8216 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0008× [0.9955, 1.0073].
  - other_buffers: 1.2940× [1.2862, 1.3016].
- S2: S2 products; [1024, 1024, 4608]; b2; confirmed 0.9134 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0039× [0.9993, 1.0108].
  - other_buffers: 1.2703× [1.2654, 1.2752].

### shape_m4097_k4097_n4097__bfloat16

- S1: S1 products; [1024, 512, 4608]; b2; confirmed 0.7631 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9995× [0.9932, 1.0057].
  - other_buffers: 1.2793× [1.2722, 1.2867].
- S2: S2 outputs; [1024, 1024, 4608]; b2; confirmed 0.8410 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0007× [0.9959, 1.0058].
  - other_buffers: 1.2642× [1.2587, 1.2699].

### shape_m1536_k32768_n1536__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 0.6498 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9953× [0.9848, 1.0036].
  - other_buffers: 1.2853× [1.2696, 1.2964].
- S2: S2 products; [512, 512, 8192]; b2; confirmed 0.6905 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0053× [0.9992, 1.0108].
  - other_buffers: 1.5851× [1.5747, 1.5966].

### shape_m1536_k32768_n1536__bfloat16

- S1: S1 outputs; [512, 512, 8192]; b2; confirmed 0.6302 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0011× [0.9950, 1.0083].
  - other_buffers: 1.3477× [1.3370, 1.3597].
- S2: S2 products; [512, 512, 16384]; b2; confirmed 0.6664 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9988× [0.9911, 1.0074].
  - other_buffers: 1.5567× [1.5440, 1.5680].

### shape_m3072_k8192_n3072__float32

- S1: S1 outputs; [1024, 512, 8192]; b2; confirmed 0.4767 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9462× [0.8566, 1.0051].
  - other_buffers: 1.2380× [1.1165, 1.3186].
- S2: S2 products; [1024, 1024, 8192]; b2; confirmed 0.5048 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9795× [0.9057, 1.0138].
  - other_buffers: 1.2265× [1.1317, 1.2718].

### shape_m3072_k8192_n3072__bfloat16

- S1: S1 outputs; [1024, 512, 8192]; b2; confirmed 0.4598 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9908× [0.9757, 1.0026].
  - other_buffers: 1.2785× [1.2468, 1.3188].
- S2: S2 products; [1024, 1024, 4096]; b2; confirmed 0.4987 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0044× [0.9953, 1.0151].
  - other_buffers: 1.4043× [1.3909, 1.4210].

### shape_m4608_k4608_n4608__float32

- S1: S1 products; [512, 512, 4608]; b2; confirmed 0.6048 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0126× [1.0026, 1.0265].
  - other_buffers: 1.5153× [1.5008, 1.5351].
- S2: S2 products; [512, 512, 4608]; b2; confirmed 0.7795 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0093× [1.0058, 1.0132].
  - other_buffers: 1.5306× [1.5239, 1.5379].

### shape_m4608_k4608_n4608__bfloat16

- S1: S1 outputs; [512, 512, 4608]; b2; confirmed 0.5787 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9972× [0.9916, 1.0029].
  - other_buffers: 1.5202× [1.5108, 1.5295].
- S2: S2 products; [512, 512, 4608]; b2; confirmed 0.7707 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0015× [0.9977, 1.0054].
  - other_buffers: 1.5025× [1.4961, 1.5080].

### shape_m256_k98304_n4096__float32

- S1: S1 outputs; [256, 512, 24576]; b2; confirmed 1.0422 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9993× [0.9945, 1.0050].
  - other_buffers: 1.2890× [1.2838, 1.2946].
- S2: S2 outputs; [256, 512, 24576]; b2; confirmed 1.1314 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9829× [0.9488, 0.9984].
  - other_buffers: 1.6553× [1.5955, 1.6859].

### shape_m256_k98304_n4096__bfloat16

- S1: S1 outputs; [256, 512, 24576]; b2; confirmed 1.0490 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9981× [0.9896, 1.0043].
  - other_buffers: 1.2846× [1.2753, 1.2917].
- S2: S2 outputs; [256, 512, 24576]; b2; confirmed 1.1247 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9933× [0.9857, 1.0000].
  - other_buffers: 1.6687× [1.6429, 1.6882].

### shape_m512_k16384_n12288__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 0.5553 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9948× [0.9897, 1.0003].
  - other_buffers: 1.4328× [1.4267, 1.4384].
- S2: S2 products; [512, 512, 16384]; b2; confirmed 0.7930 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0034× [0.9958, 1.0124].
  - other_buffers: 1.3606× [1.3530, 1.3680].

### shape_m512_k16384_n12288__bfloat16

- S1: S1 products; [512, 512, 16384]; b2; confirmed 0.5456 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9962× [0.9893, 1.0038].
  - other_buffers: 1.4462× [1.4373, 1.4545].
- S2: S2 products; [512, 512, 16384]; b2; confirmed 0.7995 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9908× [0.9687, 1.0023].
  - other_buffers: 1.3397× [1.3060, 1.3629].

### shape_m16384_k1024_n6144__float32

- S1: S1 outputs; [4096, 1024, 1024]; b2; confirmed 0.5779 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9894× [0.9817, 0.9951].
  - other_buffers: 1.1068× [1.0965, 1.1183].
- S2: S2 outputs; [4096, 1024, 1024]; b2; confirmed 0.5990 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9826× [0.9758, 0.9894].
  - other_buffers: 1.1880× [1.1764, 1.1988].

### shape_m16384_k1024_n6144__bfloat16

- S1: S1 products; [4096, 1024, 1024]; b2; confirmed 0.4737 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0095× [0.9896, 1.0557].
  - other_buffers: 1.2301× [1.2220, 1.2385].
- S2: S2 outputs; [4096, 1024, 1024]; b2; confirmed 0.5279 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0161× [1.0088, 1.0251].
  - other_buffers: 1.2170× [1.2103, 1.2235].

### shape_m65536_k256_n6144__float32

- S1: S1 products; [2048, 1024, 512]; b2; confirmed 1.3909 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0009× [0.9975, 1.0044].
  - other_buffers: 1.0541× [1.0508, 1.0580].
- S2: S2 outputs; [2048, 2048, 512]; b2; confirmed 1.4597 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0326× [1.0297, 1.0349].
  - other_buffers: 1.0461× [1.0438, 1.0483].

### shape_m65536_k256_n6144__bfloat16

- S1: S1 products; [2048, 2048, 512]; b2; confirmed 0.9178 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9889× [0.9824, 0.9957].
  - other_buffers: 1.0925× [1.0839, 1.0985].
- S2: S2 outputs; [2048, 1024, 512]; b2; confirmed 1.3404 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0444× [1.0402, 1.0508].
  - other_buffers: 1.0920× [1.0872, 1.0988].

### shape_m768_k24576_n6144__float32

- S1: S1 outputs; [1024, 512, 24576]; b2; confirmed 0.7165 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9987× [0.9890, 1.0066].
  - other_buffers: 1.2880× [1.2783, 1.2964].
- S2: S2 products; [1024, 2048, 6144]; b2; confirmed 0.8016 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0217× [1.0110, 1.0436].
  - other_buffers: 1.3459× [1.3362, 1.3551].

### shape_m768_k24576_n6144__bfloat16

- S1: S1 outputs; [1024, 512, 24576]; b2; confirmed 0.6779 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9990× [0.9916, 1.0077].
  - other_buffers: 1.2839× [1.2752, 1.2923].
- S2: S2 products; [1024, 1024, 6144]; b2; confirmed 0.7402 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0150× [1.0059, 1.0289].
  - other_buffers: 1.5134× [1.5045, 1.5237].

### shape_m5120_k5120_n5120__float32

- S1: S1 products; [1024, 512, 5120]; b2; confirmed 0.5728 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0115× [1.0064, 1.0167].
  - other_buffers: 1.5077× [1.5003, 1.5143].
- S2: S2 outputs; [1024, 2560, 5120]; b2; confirmed 0.6389 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.3954× [1.3890, 1.4023].

### shape_m5120_k5120_n5120__bfloat16

- S1: S1 outputs; [1024, 2560, 5120]; b2; confirmed 0.5376 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9997× [0.9931, 1.0075].
  - other_buffers: 1.4086× [1.3997, 1.4173].
- S2: S2 outputs; [1024, 1024, 5120]; b2; confirmed 0.6052 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0039× [0.9972, 1.0116].
  - other_buffers: 1.3963× [1.3877, 1.4051].

### shape_m256_k32768_n16384__float32

- S1: S1 outputs; [256, 512, 32768]; b2; confirmed 0.9800 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9923× [0.9719, 1.0032].
  - other_buffers: 1.3929× [1.3666, 1.4065].
- S2: S2 products; [256, 512, 16384]; b2; confirmed 1.3837 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0023× [0.9928, 1.0088].
  - other_buffers: 1.7536× [1.7404, 1.7613].

### shape_m256_k32768_n16384__bfloat16

- S1: S1 products; [256, 512, 32768]; b2; confirmed 0.9772 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9967× [0.9849, 1.0036].
  - other_buffers: 1.3953× [1.3770, 1.4066].
- S2: S2 products; [256, 512, 8192]; b2; confirmed 1.4091 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9977× [0.9898, 1.0043].
  - other_buffers: 1.7787× [1.7675, 1.7869].

### shape_m2048_k2048_n32768__float32

- S1: S1 outputs; [2048, 1024, 2048]; b2; confirmed 0.5693 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9636× [0.9012, 0.9898].
  - other_buffers: 1.3556× [1.2693, 1.3964].
- S2: S2 products; [2048, 1024, 2048]; b2; confirmed 0.5998 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0104× [0.9982, 1.0322].
  - other_buffers: 1.3557× [1.3472, 1.3634].

### shape_m2048_k2048_n32768__bfloat16

- S1: S1 products; [2048, 2048, 2048]; b2; confirmed 0.5504 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0022× [0.9937, 1.0107].
  - other_buffers: 1.3459× [1.3390, 1.3523].
- S2: S2 products; [2048, 1024, 2048]; b2; confirmed 0.5987 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9958× [0.9849, 1.0151].
  - other_buffers: 1.3469× [1.3355, 1.3595].

### shape_m2048_k32768_n2048__float32

- S1: S1 products; [2048, 2048, 1024]; b2; confirmed 0.5447 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0910× [1.0832, 1.0999].
  - other_buffers: 1.3567× [1.3456, 1.3687].
- S2: S2 products; [2048, 2048, 1024]; b2; confirmed 0.6111 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0655× [1.0586, 1.0731].
  - other_buffers: 1.3021× [1.2916, 1.3134].

### shape_m2048_k32768_n2048__bfloat16

- S1: S1 outputs; [2048, 2048, 1024]; b2; confirmed 0.5548 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9925× [0.9857, 0.9990].
  - other_buffers: 1.3432× [1.3336, 1.3534].
- S2: S2 products; [2048, 2048, 1024]; b2; confirmed 0.6124 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0873× [1.0799, 1.0956].
  - other_buffers: 1.3058× [1.2989, 1.3141].

### shape_m32768_k2048_n2048__float32

- S1: S1 products; [2048, 2048, 2048]; b2; confirmed 0.5619 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0107× [0.9955, 1.0227].
  - other_buffers: 1.3436× [1.3241, 1.3610].
- S2: S2 outputs; [2048, 2048, 2048]; b2; confirmed 0.6137 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0120× [1.0039, 1.0194].
  - other_buffers: 1.3139× [1.3055, 1.3213].

### shape_m32768_k2048_n2048__bfloat16

- S1: S1 outputs; [2048, 2048, 2048]; b2; confirmed 0.5403 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0029× [0.9964, 1.0093].
  - other_buffers: 1.3502× [1.3404, 1.3627].
- S2: S2 outputs; [4096, 1024, 2048]; b2; confirmed 0.5862 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9950× [0.9780, 1.0053].
  - other_buffers: 1.3776× [1.3230, 1.4601].

### shape_m131072_k1024_n1024__float32

- S1: S1 products; [4096, 1024, 1024]; b2; confirmed 0.8009 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0004× [0.9963, 1.0045].
  - other_buffers: 1.2178× [1.2112, 1.2251].
- S2: S2 outputs; [4096, 1024, 1024]; b2; confirmed 0.8072 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0004× [0.9950, 1.0059].
  - other_buffers: 1.3469× [1.3355, 1.3560].

### shape_m131072_k1024_n1024__bfloat16

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.6292 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9942× [0.9890, 0.9998].
  - other_buffers: 1.5579× [1.5481, 1.5668].
- S2: S2 products; [4096, 1024, 1024]; b2; confirmed 0.6534 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9946× [0.9882, 1.0026].
  - other_buffers: 1.5679× [1.5612, 1.5753].

### shape_m1536_k24576_n4096__float32

- S1: S1 products; [512, 512, 24576]; b2; confirmed 0.7098 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9992× [0.9954, 1.0027].
  - other_buffers: 1.4950× [1.4832, 1.5062].
- S2: S2 products; [2048, 1024, 6144]; b2; confirmed 0.8915 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0189× [1.0144, 1.0242].
  - other_buffers: 1.4200× [1.4156, 1.4238].

### shape_m1536_k24576_n4096__bfloat16

- S1: S1 outputs; [512, 512, 24576]; b2; confirmed 0.7066 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9968× [0.9917, 1.0022].
  - other_buffers: 1.4933× [1.4869, 1.5003].
- S2: S2 products; [2048, 1024, 6144]; b2; confirmed 0.8696 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0051× [0.9943, 1.0140].
  - other_buffers: 1.4319× [1.4126, 1.4483].

### shape_m1536_k65536_n1536__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 1.0474 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0009× [0.9971, 1.0047].
  - other_buffers: 1.3684× [1.3591, 1.3824].
- S2: S2 outputs; [512, 512, 16384]; b2; confirmed 1.0911 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0023× [0.9981, 1.0067].
  - other_buffers: 1.7011× [1.6923, 1.7102].

### shape_m1536_k65536_n1536__bfloat16

- S1: S1 products; [512, 512, 16384]; b2; confirmed 1.0318 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9984× [0.9949, 1.0020].
  - other_buffers: 1.3722× [1.3626, 1.3819].
- S2: S2 outputs; [512, 512, 16384]; b2; confirmed 1.0783 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9996× [0.9965, 1.0027].
  - other_buffers: 1.7049× [1.6977, 1.7123].

### shape_m3072_k16384_n3072__float32

- S1: S1 products; [1024, 512, 16384]; b2; confirmed 0.6412 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0008× [0.9888, 1.0091].
  - other_buffers: 1.3708× [1.3591, 1.3793].
- S2: S2 outputs; [1024, 1024, 8192]; b2; confirmed 0.7288 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9946× [0.9818, 1.0024].
  - other_buffers: 1.5138× [1.4933, 1.5250].

### shape_m3072_k16384_n3072__bfloat16

- S1: S1 products; [1024, 512, 16384]; b2; confirmed 0.6385 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9998× [0.9917, 1.0092].
  - other_buffers: 1.3465× [1.3378, 1.3555].
- S2: S2 products; [1024, 1024, 4096]; b2; confirmed 0.7185 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9904× [0.9383, 1.0128].
  - other_buffers: 1.5447× [1.4589, 1.5820].

### shape_m2048_k32768_n3072__float32

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.7243 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1192× [1.1145, 1.1242].
  - other_buffers: 1.6922× [1.6461, 1.7692].
- S2: S2 products; [1024, 1024, 8192]; b2; confirmed 0.8526 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0086× [1.0044, 1.0131].
  - other_buffers: 1.5862× [1.5742, 1.5962].

### shape_m2048_k32768_n3072__bfloat16

- S1: S1 products; [2048, 1024, 1024]; b2; confirmed 0.7219 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0220× [1.0166, 1.0272].
  - other_buffers: 1.6583× [1.6463, 1.6699].
- S2: S2 products; [1024, 1024, 8192]; b2; confirmed 0.8443 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0020× [0.9966, 1.0070].
  - other_buffers: 1.5930× [1.5821, 1.6050].

### shape_m3072_k32768_n2048__float32

- S1: S1 products; [1024, 2048, 1024]; b2; confirmed 0.7632 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1090× [1.0922, 1.1507].
  - other_buffers: 1.5872× [1.5776, 1.5969].
- S2: S2 products; [1024, 1024, 8192]; b2; confirmed 0.8481 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0133× [1.0086, 1.0177].
  - other_buffers: 1.5863× [1.5728, 1.5985].

### shape_m3072_k32768_n2048__bfloat16

- S1: S1 products; [1024, 2048, 1024]; b2; confirmed 0.7597 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0361× [1.0246, 1.0444].
  - other_buffers: 1.5925× [1.5807, 1.6034].
- S2: S2 outputs; [1024, 1024, 8192]; b2; confirmed 0.8455 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9981× [0.9931, 1.0030].
  - other_buffers: 1.5939× [1.5819, 1.6120].

### shape_m4096_k2048_n24576__float32

- S1: S1 products; [2048, 2048, 2048]; b2; confirmed 0.7236 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0194× [1.0142, 1.0250].
  - other_buffers: 1.4395× [1.4212, 1.4763].
- S2: S2 outputs; [4096, 1024, 2048]; b2; confirmed 0.7681 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0108× [1.0058, 1.0157].
  - other_buffers: 1.2130× [1.2064, 1.2200].

### shape_m4096_k2048_n24576__bfloat16

- S1: S1 outputs; [2048, 2048, 2048]; b2; confirmed 0.6779 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0000× [0.9937, 1.0066].
  - other_buffers: 1.4484× [1.4403, 1.4566].
- S2: S2 outputs; [4096, 1024, 2048]; b2; confirmed 0.7280 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0018× [0.9911, 1.0086].
  - other_buffers: 1.2280× [1.2167, 1.2363].

### shape_m4096_k131072_n384__float32

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 1.5294 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0288× [1.0260, 1.0316].
  - other_buffers: 1.6643× [1.6576, 1.6703].
- S2: S2 products; [1024, 512, 1024]; b2; confirmed 1.8616 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1036× [1.1011, 1.1063].
  - other_buffers: 1.6955× [1.6888, 1.7032].

### shape_m4096_k131072_n384__bfloat16

- S1: S1 products; [1024, 512, 1024]; b2; confirmed 1.5368 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0150× [0.9910, 1.0393].
  - other_buffers: 1.6562× [1.6179, 1.6717].
- S2: S2 products; [1024, 512, 1024]; b2; confirmed 1.8605 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0580× [1.0553, 1.0607].
  - other_buffers: 1.6981× [1.6915, 1.7087].

### shape_m768_k49152_n6144__float32

- S1: S1 products; [1024, 2048, 1024]; b2; confirmed 1.1555 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1018× [1.0944, 1.1083].
  - other_buffers: 1.6074× [1.5973, 1.6157].
- S2: S2 products; [1024, 2048, 1024]; b2; confirmed 1.3541 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0555× [1.0529, 1.0582].
  - other_buffers: 1.5234× [1.5204, 1.5268].

### shape_m768_k49152_n6144__bfloat16

- S1: S1 products; [1024, 2048, 1024]; b2; confirmed 1.1273 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0410× [1.0375, 1.0443].
  - other_buffers: 1.6201× [1.6145, 1.6260].
- S2: S2 products; [1024, 2048, 1024]; b2; confirmed 1.3347 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0835× [1.0810, 1.0859].
  - other_buffers: 1.5254× [1.5194, 1.5312].

### shape_m2048_k2048_n65536__float32

- S1: S1 products; [2048, 2048, 2048]; b2; confirmed 0.8535 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0213× [1.0163, 1.0264].
  - other_buffers: 1.4674× [1.4598, 1.4751].
- S2: S2 outputs; [2048, 1024, 2048]; b2; confirmed 0.9618 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9958× [0.9905, 0.9996].
  - other_buffers: 1.4533× [1.4460, 1.4628].

### shape_m2048_k2048_n65536__bfloat16

- S1: S1 outputs; [2048, 2048, 2048]; b2; confirmed 0.8330 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0038× [0.9995, 1.0081].
  - other_buffers: 1.4785× [1.4714, 1.4855].
- S2: S2 products; [2048, 1024, 2048]; b2; confirmed 0.9434 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9872× [0.9841, 0.9905].
  - other_buffers: 1.4422× [1.4360, 1.4473].

### shape_m2048_k65536_n2048__float32

- S1: S1 products; [2048, 2048, 1024]; b2; confirmed 0.8300 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1176× [1.1103, 1.1238].
  - other_buffers: 1.4672× [1.4513, 1.4823].
- S2: S2 products; [2048, 2048, 1024]; b2; confirmed 0.9591 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0820× [1.0723, 1.0898].
  - other_buffers: 1.4126× [1.3813, 1.4808].

### shape_m2048_k65536_n2048__bfloat16

- S1: S1 products; [1024, 2048, 512]; b2; confirmed 0.9490 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1651× [1.1465, 1.1748].
  - other_buffers: 1.6942× [1.6690, 1.7071].
- S2: S2 products; [2048, 2048, 1024]; b2; confirmed 0.9704 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.1144× [1.0933, 1.1430].
  - other_buffers: 1.3846× [1.3633, 1.4002].

### shape_m4096_k8192_n8192__float32

- S1: S1 outputs; [1024, 512, 8192]; b2; confirmed 0.8881 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9930× [0.9859, 0.9996].
  - other_buffers: 1.5589× [1.5478, 1.5680].
- S2: S2 products; [2048, 2048, 2048]; b2; confirmed 0.9420 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0772× [1.0712, 1.0859].
  - other_buffers: 1.4556× [1.4474, 1.4660].

### shape_m4096_k8192_n8192__bfloat16

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 0.8749 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.4484× [1.4272, 1.4931].
- S2: S2 products; [4096, 1024, 2048]; b2; confirmed 0.8780 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0427× [1.0378, 1.0481].
  - other_buffers: 1.5485× [1.5424, 1.5552].

### shape_m4096_k16384_n4096__float32

- S1: S1 products; [2048, 2048, 1024]; b2; confirmed 0.8779 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0984× [1.0929, 1.1047].
  - other_buffers: 1.4751× [1.4680, 1.4828].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.9315 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0368× [1.0327, 1.0406].
  - other_buffers: 1.5789× [1.5646, 1.5911].

### shape_m4096_k16384_n4096__bfloat16

- S1: S1 products; [2048, 2048, 1024]; b2; confirmed 0.9010 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9879× [0.9184, 1.0160].
  - other_buffers: 1.4543× [1.3550, 1.4980].
- S2: S2 products; [2048, 1024, 4096]; b2; confirmed 0.9231 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0240× [1.0165, 1.0303].
  - other_buffers: 1.5991× [1.5695, 1.6415].

### shape_m8192_k4096_n8192__float32

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 0.8738 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.4567× [1.4478, 1.4643].
- S2: S2 outputs; [2048, 2048, 4096]; b2; confirmed 0.9308 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.4151× [1.4080, 1.4226].

### shape_m8192_k4096_n8192__bfloat16

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 0.8338 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0324× [0.9966, 1.1284].
  - other_buffers: 1.3721× [1.3640, 1.3803].
- S2: S2 outputs; [2048, 1024, 4096]; b2; confirmed 0.9123 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9754× [0.8965, 1.0072].
  - other_buffers: 1.3320× [1.2193, 1.3790].

### shape_m8192_k8192_n4096__float32

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 0.8916 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.4755× [1.4696, 1.4814].
- S2: S2 products; [2048, 2048, 2048]; b2; confirmed 0.9424 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0743× [1.0679, 1.0802].
  - other_buffers: 1.4555× [1.4471, 1.4625].

### shape_m8192_k8192_n4096__bfloat16

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 0.8703 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.4754× [1.4351, 1.5667].
- S2: S2 products; [4096, 1024, 2048]; b2; confirmed 0.8763 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0416× [1.0373, 1.0461].
  - other_buffers: 1.5504× [1.5442, 1.5568].

### shape_m65536_k2048_n2048__float32

- S1: S1 products; [2048, 2048, 2048]; b2; confirmed 0.8741 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0069× [0.9532, 1.0332].
  - other_buffers: 1.4453× [1.3707, 1.4780].
- S2: S2 outputs; [2048, 2048, 2048]; b2; confirmed 0.9687 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0160× [1.0114, 1.0224].
  - other_buffers: 1.4151× [1.4101, 1.4209].

### shape_m65536_k2048_n2048__bfloat16

- S1: S1 outputs; [2048, 2048, 2048]; b2; confirmed 0.8378 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0013× [0.9965, 1.0057].
  - other_buffers: 1.4677× [1.4624, 1.4728].
- S2: S2 outputs; [4096, 1024, 2048]; b2; confirmed 0.9179 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0024× [0.9987, 1.0060].
  - other_buffers: 1.4595× [1.4522, 1.4666].

### shape_m384_k12288_n65536__float32

- S1: S1 products; [512, 512, 12288]; b2; confirmed 1.5404 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9986× [0.9952, 1.0019].
  - other_buffers: 1.6747× [1.6709, 1.6786].
- S2: S2 outputs; [512, 512, 12288]; b2; confirmed 2.5716 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9882× [0.9860, 0.9900].
  - other_buffers: 1.4761× [1.4737, 1.4781].

### shape_m384_k12288_n65536__bfloat16

- S1: S1 outputs; [512, 512, 12288]; b2; confirmed 1.4219 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0000× [0.9965, 1.0032].
  - other_buffers: 1.7389× [1.7303, 1.7472].
- S2: S2 outputs; [512, 512, 12288]; b2; confirmed 2.4840 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9995× [0.9976, 1.0014].
  - other_buffers: 1.4774× [1.4750, 1.4799].

### shape_m384_k65536_n12288__float32

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 2.4868 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 0.9959× [0.9782, 1.0037].
  - other_buffers: 1.4049× [1.3779, 1.4161].
- S2: S2 products; [512, 512, 16384]; b2; confirmed 2.5553 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0029× [1.0004, 1.0065].
  - other_buffers: 1.8048× [1.8013, 1.8086].

### shape_m384_k65536_n12288__bfloat16

- S1: S1 outputs; [512, 512, 16384]; b2; confirmed 2.4306 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0005× [0.9984, 1.0026].
  - other_buffers: 1.4261× [1.4172, 1.4472].
- S2: S2 products; [512, 512, 16384]; b2; confirmed 2.5184 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0013× [0.9978, 1.0056].
  - other_buffers: 1.8163× [1.8118, 1.8202].

### shape_m1536_k131072_n1536__float32

- S1: S1 products; [512, 512, 1024]; b2; confirmed 2.1001 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0339× [1.0306, 1.0372].
  - other_buffers: 1.8119× [1.8044, 1.8195].
- S2: S2 products; [512, 512, 1024]; b2; confirmed 2.4363 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0383× [1.0337, 1.0420].
  - other_buffers: 1.8779× [1.8691, 1.8903].

### shape_m1536_k131072_n1536__bfloat16

- S1: S1 products; [512, 512, 1024]; b2; confirmed 2.0964 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0170× [1.0035, 1.0242].
  - other_buffers: 1.8078× [1.7830, 1.8189].
- S2: S2 products; [512, 512, 1024]; b2; confirmed 2.4286 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0205× [1.0176, 1.0238].
  - other_buffers: 1.8735× [1.8696, 1.8771].

### shape_m8192_k8192_n8192__float32

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 1.4867 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.5937× [1.5895, 1.5983].
- S2: S2 products; [4096, 1024, 2048]; b2; confirmed 1.6003 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0945× [1.0916, 1.0970].
  - other_buffers: 1.5995× [1.5937, 1.6055].

### shape_m8192_k8192_n8192__bfloat16

- S1: S1 outputs; [2048, 2048, 4096]; b2; confirmed 1.4979 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: comparison ineligible/unavailable; outcomes ['oom', 'oom', 'oom'].
  - other_buffers: 1.5207× [1.4798, 1.5383].
- S2: S2 products; [4096, 1024, 2048]; b2; confirmed 1.5131 ms. Selected by the lowest eligible batch-normalized screening latency across both accumulator strategies, K-panel lengths and buffer counts.
  - other_accumulator: 1.0490× [1.0439, 1.0544].
  - other_buffers: 1.6465× [1.6402, 1.6530].

## Coverage

All planned outcomes present: False.
{'screen': {'ok': 44444, 'oom': 2695}, 'confirm': {'ok': 9945, 'oom': 60}}
candidate_decisions.json retains offered/pruned configurations, memory estimates, omitted K divisors, numerical checks, screening anchors, ranks and frozen choices. results.json retains every confirmation arm and comparison, including previous controls. tuner_policy.json is a research recommendation table, not an installed serving dispatcher.
Compiled HLO and cost metadata are preserved in each phase. Memory estimates are search heuristics; no performance cause is inferred from them alone.

