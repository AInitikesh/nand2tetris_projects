
// init
	@256 // 0
	D=A // 1
	@SP // 2
	M=D // 3
// call Sys.init 0
	@Sys.init$ret.1 // 4
	D=A // 5
	@SP // 6
	A=M // 7
	M=D // 8
	@SP // 9
	M=M+1 // 10
// C_PUSH location LCL
	@LCL // 11
	D=M // 12
	@SP // 13
	A=M // 14
	M=D // 15
	@SP // 16
	M=M+1 // 17
// C_PUSH location ARG
	@ARG // 18
	D=M // 19
	@SP // 20
	A=M // 21
	M=D // 22
	@SP // 23
	M=M+1 // 24
// C_PUSH pointer 0
	@THIS // 25
	D=M // 26
	@SP // 27
	A=M // 28
	M=D // 29
	@SP // 30
	M=M+1 // 31
// C_PUSH pointer 1
	@THAT // 32
	D=M // 33
	@SP // 34
	A=M // 35
	M=D // 36
	@SP // 37
	M=M+1 // 38
	@SP // 39
	D=M // 40
	@5 // 41
	D=D-A // 42
	@0 // 43
	D=D-A // 44
	@ARG // 45
	M=D // 46
	@SP // 47
	D=M // 48
	@LCL // 49
	M=D // 50
// goto Sys.init
	@Sys.init // 51
	0;JMP // 52
(Sys.init$ret.1)
// function Sys.init 0
(Sys.init)
// C_PUSH constant 4000
	@4000 // 53
	D=A // 54
	@SP // 55
	A=M // 56
	M=D // 57
	@SP // 58
	M=M+1 // 59
// C_POP pointer 0
	@SP // 60
	M=M-1 // 61
	A=M // 62
	D=M // 63
	@THIS // 64
	M=D // 65
// C_PUSH constant 5000
	@5000 // 66
	D=A // 67
	@SP // 68
	A=M // 69
	M=D // 70
	@SP // 71
	M=M+1 // 72
// C_POP pointer 1
	@SP // 73
	M=M-1 // 74
	A=M // 75
	D=M // 76
	@THAT // 77
	M=D // 78
// call Sys.main 0
	@Sys.main$ret.1 // 79
	D=A // 80
	@SP // 81
	A=M // 82
	M=D // 83
	@SP // 84
	M=M+1 // 85
// C_PUSH location LCL
	@LCL // 86
	D=M // 87
	@SP // 88
	A=M // 89
	M=D // 90
	@SP // 91
	M=M+1 // 92
// C_PUSH location ARG
	@ARG // 93
	D=M // 94
	@SP // 95
	A=M // 96
	M=D // 97
	@SP // 98
	M=M+1 // 99
// C_PUSH pointer 0
	@THIS // 100
	D=M // 101
	@SP // 102
	A=M // 103
	M=D // 104
	@SP // 105
	M=M+1 // 106
// C_PUSH pointer 1
	@THAT // 107
	D=M // 108
	@SP // 109
	A=M // 110
	M=D // 111
	@SP // 112
	M=M+1 // 113
	@SP // 114
	D=M // 115
	@5 // 116
	D=D-A // 117
	@0 // 118
	D=D-A // 119
	@ARG // 120
	M=D // 121
	@SP // 122
	D=M // 123
	@LCL // 124
	M=D // 125
// goto Sys.main
	@Sys.main // 126
	0;JMP // 127
(Sys.main$ret.1)
// C_POP temp 1
	@SP // 128
	M=M-1 // 129
	A=M // 130
	D=M // 131
	@R6 // 132
	M=D // 133
(Sys.init$LOOP)
// goto Sys.init$LOOP
	@Sys.init$LOOP // 134
	0;JMP // 135
// function Sys.main 5
(Sys.main)
	@SP // 136
	A=M // 137
	M=0 // 138
	@SP // 139
	M=M+1 // 140
	@SP // 141
	A=M // 142
	M=0 // 143
	@SP // 144
	M=M+1 // 145
	@SP // 146
	A=M // 147
	M=0 // 148
	@SP // 149
	M=M+1 // 150
	@SP // 151
	A=M // 152
	M=0 // 153
	@SP // 154
	M=M+1 // 155
	@SP // 156
	A=M // 157
	M=0 // 158
	@SP // 159
	M=M+1 // 160
// C_PUSH constant 4001
	@4001 // 161
	D=A // 162
	@SP // 163
	A=M // 164
	M=D // 165
	@SP // 166
	M=M+1 // 167
// C_POP pointer 0
	@SP // 168
	M=M-1 // 169
	A=M // 170
	D=M // 171
	@THIS // 172
	M=D // 173
// C_PUSH constant 5001
	@5001 // 174
	D=A // 175
	@SP // 176
	A=M // 177
	M=D // 178
	@SP // 179
	M=M+1 // 180
// C_POP pointer 1
	@SP // 181
	M=M-1 // 182
	A=M // 183
	D=M // 184
	@THAT // 185
	M=D // 186
// C_PUSH constant 200
	@200 // 187
	D=A // 188
	@SP // 189
	A=M // 190
	M=D // 191
	@SP // 192
	M=M+1 // 193
// C_POP local 1
	@1 // 194
	D=A // 195
	@LCL // 196
	D=M+D // 197
	@R13 // 198
	M=D // 199
	@SP // 200
	M=M-1 // 201
	A=M // 202
	D=M // 203
	@R13 // 204
	A=M // 205
	M=D // 206
// C_PUSH constant 40
	@40 // 207
	D=A // 208
	@SP // 209
	A=M // 210
	M=D // 211
	@SP // 212
	M=M+1 // 213
// C_POP local 2
	@2 // 214
	D=A // 215
	@LCL // 216
	D=M+D // 217
	@R13 // 218
	M=D // 219
	@SP // 220
	M=M-1 // 221
	A=M // 222
	D=M // 223
	@R13 // 224
	A=M // 225
	M=D // 226
// C_PUSH constant 6
	@6 // 227
	D=A // 228
	@SP // 229
	A=M // 230
	M=D // 231
	@SP // 232
	M=M+1 // 233
// C_POP local 3
	@3 // 234
	D=A // 235
	@LCL // 236
	D=M+D // 237
	@R13 // 238
	M=D // 239
	@SP // 240
	M=M-1 // 241
	A=M // 242
	D=M // 243
	@R13 // 244
	A=M // 245
	M=D // 246
// C_PUSH constant 123
	@123 // 247
	D=A // 248
	@SP // 249
	A=M // 250
	M=D // 251
	@SP // 252
	M=M+1 // 253
// call Sys.add12 1
	@Sys.add12$ret.1 // 254
	D=A // 255
	@SP // 256
	A=M // 257
	M=D // 258
	@SP // 259
	M=M+1 // 260
// C_PUSH location LCL
	@LCL // 261
	D=M // 262
	@SP // 263
	A=M // 264
	M=D // 265
	@SP // 266
	M=M+1 // 267
// C_PUSH location ARG
	@ARG // 268
	D=M // 269
	@SP // 270
	A=M // 271
	M=D // 272
	@SP // 273
	M=M+1 // 274
// C_PUSH pointer 0
	@THIS // 275
	D=M // 276
	@SP // 277
	A=M // 278
	M=D // 279
	@SP // 280
	M=M+1 // 281
// C_PUSH pointer 1
	@THAT // 282
	D=M // 283
	@SP // 284
	A=M // 285
	M=D // 286
	@SP // 287
	M=M+1 // 288
	@SP // 289
	D=M // 290
	@5 // 291
	D=D-A // 292
	@1 // 293
	D=D-A // 294
	@ARG // 295
	M=D // 296
	@SP // 297
	D=M // 298
	@LCL // 299
	M=D // 300
// goto Sys.add12
	@Sys.add12 // 301
	0;JMP // 302
(Sys.add12$ret.1)
// C_POP temp 0
	@SP // 303
	M=M-1 // 304
	A=M // 305
	D=M // 306
	@R5 // 307
	M=D // 308
// C_PUSH local 0
	@0 // 309
	D=A // 310
	@LCL // 311
	A=M+D // 312
	D=M // 313
	@SP // 314
	A=M // 315
	M=D // 316
	@SP // 317
	M=M+1 // 318
// C_PUSH local 1
	@1 // 319
	D=A // 320
	@LCL // 321
	A=M+D // 322
	D=M // 323
	@SP // 324
	A=M // 325
	M=D // 326
	@SP // 327
	M=M+1 // 328
// C_PUSH local 2
	@2 // 329
	D=A // 330
	@LCL // 331
	A=M+D // 332
	D=M // 333
	@SP // 334
	A=M // 335
	M=D // 336
	@SP // 337
	M=M+1 // 338
// C_PUSH local 3
	@3 // 339
	D=A // 340
	@LCL // 341
	A=M+D // 342
	D=M // 343
	@SP // 344
	A=M // 345
	M=D // 346
	@SP // 347
	M=M+1 // 348
// C_PUSH local 4
	@4 // 349
	D=A // 350
	@LCL // 351
	A=M+D // 352
	D=M // 353
	@SP // 354
	A=M // 355
	M=D // 356
	@SP // 357
	M=M+1 // 358
// add
	@SP // 359
	M=M-1 // 360
	@SP // 361
	A=M // 362
	D=M // 363
	@SP // 364
	M=M-1 // 365
	@SP // 366
	A=M // 367
	M=M+D // 368
	@SP // 369
	M=M+1 // 370
// add
	@SP // 371
	M=M-1 // 372
	@SP // 373
	A=M // 374
	D=M // 375
	@SP // 376
	M=M-1 // 377
	@SP // 378
	A=M // 379
	M=M+D // 380
	@SP // 381
	M=M+1 // 382
// add
	@SP // 383
	M=M-1 // 384
	@SP // 385
	A=M // 386
	D=M // 387
	@SP // 388
	M=M-1 // 389
	@SP // 390
	A=M // 391
	M=M+D // 392
	@SP // 393
	M=M+1 // 394
// add
	@SP // 395
	M=M-1 // 396
	@SP // 397
	A=M // 398
	D=M // 399
	@SP // 400
	M=M-1 // 401
	@SP // 402
	A=M // 403
	M=M+D // 404
	@SP // 405
	M=M+1 // 406
// return
	@LCL // 407
	D=M // 408
	@R13 // 409
	M=D // 410
	@5 // 411
	D=D-A // 412
	A=D // 413
	D=M // 414
	@R14 // 415
	M=D // 416
	@SP // 417
	M=M-1 // 418
	A=M // 419
	D=M // 420
	@ARG // 421
	A=M // 422
	M=D // 423
	@ARG // 424
	D=M+1 // 425
	@SP // 426
	M=D // 427
	@R13 // 428
	A=M-1 // 429
	D=M // 430
	@THAT // 431
	M=D // 432
	@R2 // 433
	D=A // 434
	@R13 // 435
	A=M-D // 436
	D=M // 437
	@THIS // 438
	M=D // 439
	@R3 // 440
	D=A // 441
	@R13 // 442
	A=M-D // 443
	D=M // 444
	@ARG // 445
	M=D // 446
	@R4 // 447
	D=A // 448
	@R13 // 449
	A=M-D // 450
	D=M // 451
	@LCL // 452
	M=D // 453
	@R14 // 454
	A=M // 455
	0;JMP // 456
// function Sys.add12 0
(Sys.add12)
// C_PUSH constant 4002
	@4002 // 457
	D=A // 458
	@SP // 459
	A=M // 460
	M=D // 461
	@SP // 462
	M=M+1 // 463
// C_POP pointer 0
	@SP // 464
	M=M-1 // 465
	A=M // 466
	D=M // 467
	@THIS // 468
	M=D // 469
// C_PUSH constant 5002
	@5002 // 470
	D=A // 471
	@SP // 472
	A=M // 473
	M=D // 474
	@SP // 475
	M=M+1 // 476
// C_POP pointer 1
	@SP // 477
	M=M-1 // 478
	A=M // 479
	D=M // 480
	@THAT // 481
	M=D // 482
// C_PUSH argument 0
	@0 // 483
	D=A // 484
	@ARG // 485
	A=M+D // 486
	D=M // 487
	@SP // 488
	A=M // 489
	M=D // 490
	@SP // 491
	M=M+1 // 492
// C_PUSH constant 12
	@12 // 493
	D=A // 494
	@SP // 495
	A=M // 496
	M=D // 497
	@SP // 498
	M=M+1 // 499
// add
	@SP // 500
	M=M-1 // 501
	@SP // 502
	A=M // 503
	D=M // 504
	@SP // 505
	M=M-1 // 506
	@SP // 507
	A=M // 508
	M=M+D // 509
	@SP // 510
	M=M+1 // 511
// return
	@LCL // 512
	D=M // 513
	@R13 // 514
	M=D // 515
	@5 // 516
	D=D-A // 517
	A=D // 518
	D=M // 519
	@R14 // 520
	M=D // 521
	@SP // 522
	M=M-1 // 523
	A=M // 524
	D=M // 525
	@ARG // 526
	A=M // 527
	M=D // 528
	@ARG // 529
	D=M+1 // 530
	@SP // 531
	M=D // 532
	@R13 // 533
	A=M-1 // 534
	D=M // 535
	@THAT // 536
	M=D // 537
	@R2 // 538
	D=A // 539
	@R13 // 540
	A=M-D // 541
	D=M // 542
	@THIS // 543
	M=D // 544
	@R3 // 545
	D=A // 546
	@R13 // 547
	A=M-D // 548
	D=M // 549
	@ARG // 550
	M=D // 551
	@R4 // 552
	D=A // 553
	@R13 // 554
	A=M-D // 555
	D=M // 556
	@LCL // 557
	M=D // 558
	@R14 // 559
	A=M // 560
	0;JMP // 561