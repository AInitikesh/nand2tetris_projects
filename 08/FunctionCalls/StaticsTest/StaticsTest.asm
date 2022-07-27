
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
// function Class1.set 0
(Class1.set)
// C_PUSH argument 0
	@0 // 53
	D=A // 54
	@ARG // 55
	A=M+D // 56
	D=M // 57
	@SP // 58
	A=M // 59
	M=D // 60
	@SP // 61
	M=M+1 // 62
// C_POP static 0
	@SP // 63
	M=M-1 // 64
	A=M // 65
	D=M // 66
	@Class1.0 // 67
	M=D // 68
// C_PUSH argument 1
	@1 // 69
	D=A // 70
	@ARG // 71
	A=M+D // 72
	D=M // 73
	@SP // 74
	A=M // 75
	M=D // 76
	@SP // 77
	M=M+1 // 78
// C_POP static 1
	@SP // 79
	M=M-1 // 80
	A=M // 81
	D=M // 82
	@Class1.1 // 83
	M=D // 84
// C_PUSH constant 0
	@0 // 85
	D=A // 86
	@SP // 87
	A=M // 88
	M=D // 89
	@SP // 90
	M=M+1 // 91
// return
	@LCL // 92
	D=M // 93
	@R13 // 94
	M=D // 95
	@5 // 96
	D=D-A // 97
	A=D // 98
	D=M // 99
	@R14 // 100
	M=D // 101
	@SP // 102
	M=M-1 // 103
	A=M // 104
	D=M // 105
	@ARG // 106
	A=M // 107
	M=D // 108
	@ARG // 109
	D=M+1 // 110
	@SP // 111
	M=D // 112
	@R13 // 113
	A=M-1 // 114
	D=M // 115
	@THAT // 116
	M=D // 117
	@R2 // 118
	D=A // 119
	@R13 // 120
	A=M-D // 121
	D=M // 122
	@THIS // 123
	M=D // 124
	@R3 // 125
	D=A // 126
	@R13 // 127
	A=M-D // 128
	D=M // 129
	@ARG // 130
	M=D // 131
	@R4 // 132
	D=A // 133
	@R13 // 134
	A=M-D // 135
	D=M // 136
	@LCL // 137
	M=D // 138
	@R14 // 139
	A=M // 140
	0;JMP // 141
// function Class1.get 0
(Class1.get)
// C_PUSH static 0
	@Class1.0 // 142
	D=M // 143
	@SP // 144
	A=M // 145
	M=D // 146
	@SP // 147
	M=M+1 // 148
// C_PUSH static 1
	@Class1.1 // 149
	D=M // 150
	@SP // 151
	A=M // 152
	M=D // 153
	@SP // 154
	M=M+1 // 155
// sub
	@SP // 156
	M=M-1 // 157
	@SP // 158
	A=M // 159
	D=M // 160
	@SP // 161
	M=M-1 // 162
	@SP // 163
	A=M // 164
	M=M-D // 165
	@SP // 166
	M=M+1 // 167
// return
	@LCL // 168
	D=M // 169
	@R13 // 170
	M=D // 171
	@5 // 172
	D=D-A // 173
	A=D // 174
	D=M // 175
	@R14 // 176
	M=D // 177
	@SP // 178
	M=M-1 // 179
	A=M // 180
	D=M // 181
	@ARG // 182
	A=M // 183
	M=D // 184
	@ARG // 185
	D=M+1 // 186
	@SP // 187
	M=D // 188
	@R13 // 189
	A=M-1 // 190
	D=M // 191
	@THAT // 192
	M=D // 193
	@R2 // 194
	D=A // 195
	@R13 // 196
	A=M-D // 197
	D=M // 198
	@THIS // 199
	M=D // 200
	@R3 // 201
	D=A // 202
	@R13 // 203
	A=M-D // 204
	D=M // 205
	@ARG // 206
	M=D // 207
	@R4 // 208
	D=A // 209
	@R13 // 210
	A=M-D // 211
	D=M // 212
	@LCL // 213
	M=D // 214
	@R14 // 215
	A=M // 216
	0;JMP // 217
// function Sys.init 0
(Sys.init)
// C_PUSH constant 6
	@6 // 218
	D=A // 219
	@SP // 220
	A=M // 221
	M=D // 222
	@SP // 223
	M=M+1 // 224
// C_PUSH constant 8
	@8 // 225
	D=A // 226
	@SP // 227
	A=M // 228
	M=D // 229
	@SP // 230
	M=M+1 // 231
// call Class1.set 2
	@Class1.set$ret.1 // 232
	D=A // 233
	@SP // 234
	A=M // 235
	M=D // 236
	@SP // 237
	M=M+1 // 238
// C_PUSH location LCL
	@LCL // 239
	D=M // 240
	@SP // 241
	A=M // 242
	M=D // 243
	@SP // 244
	M=M+1 // 245
// C_PUSH location ARG
	@ARG // 246
	D=M // 247
	@SP // 248
	A=M // 249
	M=D // 250
	@SP // 251
	M=M+1 // 252
// C_PUSH pointer 0
	@THIS // 253
	D=M // 254
	@SP // 255
	A=M // 256
	M=D // 257
	@SP // 258
	M=M+1 // 259
// C_PUSH pointer 1
	@THAT // 260
	D=M // 261
	@SP // 262
	A=M // 263
	M=D // 264
	@SP // 265
	M=M+1 // 266
	@SP // 267
	D=M // 268
	@5 // 269
	D=D-A // 270
	@2 // 271
	D=D-A // 272
	@ARG // 273
	M=D // 274
	@SP // 275
	D=M // 276
	@LCL // 277
	M=D // 278
// goto Class1.set
	@Class1.set // 279
	0;JMP // 280
(Class1.set$ret.1)
// C_POP temp 0
	@SP // 281
	M=M-1 // 282
	A=M // 283
	D=M // 284
	@R5 // 285
	M=D // 286
// C_PUSH constant 23
	@23 // 287
	D=A // 288
	@SP // 289
	A=M // 290
	M=D // 291
	@SP // 292
	M=M+1 // 293
// C_PUSH constant 15
	@15 // 294
	D=A // 295
	@SP // 296
	A=M // 297
	M=D // 298
	@SP // 299
	M=M+1 // 300
// call Class2.set 2
	@Class2.set$ret.1 // 301
	D=A // 302
	@SP // 303
	A=M // 304
	M=D // 305
	@SP // 306
	M=M+1 // 307
// C_PUSH location LCL
	@LCL // 308
	D=M // 309
	@SP // 310
	A=M // 311
	M=D // 312
	@SP // 313
	M=M+1 // 314
// C_PUSH location ARG
	@ARG // 315
	D=M // 316
	@SP // 317
	A=M // 318
	M=D // 319
	@SP // 320
	M=M+1 // 321
// C_PUSH pointer 0
	@THIS // 322
	D=M // 323
	@SP // 324
	A=M // 325
	M=D // 326
	@SP // 327
	M=M+1 // 328
// C_PUSH pointer 1
	@THAT // 329
	D=M // 330
	@SP // 331
	A=M // 332
	M=D // 333
	@SP // 334
	M=M+1 // 335
	@SP // 336
	D=M // 337
	@5 // 338
	D=D-A // 339
	@2 // 340
	D=D-A // 341
	@ARG // 342
	M=D // 343
	@SP // 344
	D=M // 345
	@LCL // 346
	M=D // 347
// goto Class2.set
	@Class2.set // 348
	0;JMP // 349
(Class2.set$ret.1)
// C_POP temp 0
	@SP // 350
	M=M-1 // 351
	A=M // 352
	D=M // 353
	@R5 // 354
	M=D // 355
// call Class1.get 0
	@Class1.get$ret.1 // 356
	D=A // 357
	@SP // 358
	A=M // 359
	M=D // 360
	@SP // 361
	M=M+1 // 362
// C_PUSH location LCL
	@LCL // 363
	D=M // 364
	@SP // 365
	A=M // 366
	M=D // 367
	@SP // 368
	M=M+1 // 369
// C_PUSH location ARG
	@ARG // 370
	D=M // 371
	@SP // 372
	A=M // 373
	M=D // 374
	@SP // 375
	M=M+1 // 376
// C_PUSH pointer 0
	@THIS // 377
	D=M // 378
	@SP // 379
	A=M // 380
	M=D // 381
	@SP // 382
	M=M+1 // 383
// C_PUSH pointer 1
	@THAT // 384
	D=M // 385
	@SP // 386
	A=M // 387
	M=D // 388
	@SP // 389
	M=M+1 // 390
	@SP // 391
	D=M // 392
	@5 // 393
	D=D-A // 394
	@0 // 395
	D=D-A // 396
	@ARG // 397
	M=D // 398
	@SP // 399
	D=M // 400
	@LCL // 401
	M=D // 402
// goto Class1.get
	@Class1.get // 403
	0;JMP // 404
(Class1.get$ret.1)
// call Class2.get 0
	@Class2.get$ret.1 // 405
	D=A // 406
	@SP // 407
	A=M // 408
	M=D // 409
	@SP // 410
	M=M+1 // 411
// C_PUSH location LCL
	@LCL // 412
	D=M // 413
	@SP // 414
	A=M // 415
	M=D // 416
	@SP // 417
	M=M+1 // 418
// C_PUSH location ARG
	@ARG // 419
	D=M // 420
	@SP // 421
	A=M // 422
	M=D // 423
	@SP // 424
	M=M+1 // 425
// C_PUSH pointer 0
	@THIS // 426
	D=M // 427
	@SP // 428
	A=M // 429
	M=D // 430
	@SP // 431
	M=M+1 // 432
// C_PUSH pointer 1
	@THAT // 433
	D=M // 434
	@SP // 435
	A=M // 436
	M=D // 437
	@SP // 438
	M=M+1 // 439
	@SP // 440
	D=M // 441
	@5 // 442
	D=D-A // 443
	@0 // 444
	D=D-A // 445
	@ARG // 446
	M=D // 447
	@SP // 448
	D=M // 449
	@LCL // 450
	M=D // 451
// goto Class2.get
	@Class2.get // 452
	0;JMP // 453
(Class2.get$ret.1)
(Sys.init$WHILE)
// goto Sys.init$WHILE
	@Sys.init$WHILE // 454
	0;JMP // 455
// function Class2.set 0
(Class2.set)
// C_PUSH argument 0
	@0 // 456
	D=A // 457
	@ARG // 458
	A=M+D // 459
	D=M // 460
	@SP // 461
	A=M // 462
	M=D // 463
	@SP // 464
	M=M+1 // 465
// C_POP static 0
	@SP // 466
	M=M-1 // 467
	A=M // 468
	D=M // 469
	@Class2.0 // 470
	M=D // 471
// C_PUSH argument 1
	@1 // 472
	D=A // 473
	@ARG // 474
	A=M+D // 475
	D=M // 476
	@SP // 477
	A=M // 478
	M=D // 479
	@SP // 480
	M=M+1 // 481
// C_POP static 1
	@SP // 482
	M=M-1 // 483
	A=M // 484
	D=M // 485
	@Class2.1 // 486
	M=D // 487
// C_PUSH constant 0
	@0 // 488
	D=A // 489
	@SP // 490
	A=M // 491
	M=D // 492
	@SP // 493
	M=M+1 // 494
// return
	@LCL // 495
	D=M // 496
	@R13 // 497
	M=D // 498
	@5 // 499
	D=D-A // 500
	A=D // 501
	D=M // 502
	@R14 // 503
	M=D // 504
	@SP // 505
	M=M-1 // 506
	A=M // 507
	D=M // 508
	@ARG // 509
	A=M // 510
	M=D // 511
	@ARG // 512
	D=M+1 // 513
	@SP // 514
	M=D // 515
	@R13 // 516
	A=M-1 // 517
	D=M // 518
	@THAT // 519
	M=D // 520
	@R2 // 521
	D=A // 522
	@R13 // 523
	A=M-D // 524
	D=M // 525
	@THIS // 526
	M=D // 527
	@R3 // 528
	D=A // 529
	@R13 // 530
	A=M-D // 531
	D=M // 532
	@ARG // 533
	M=D // 534
	@R4 // 535
	D=A // 536
	@R13 // 537
	A=M-D // 538
	D=M // 539
	@LCL // 540
	M=D // 541
	@R14 // 542
	A=M // 543
	0;JMP // 544
// function Class2.get 0
(Class2.get)
// C_PUSH static 0
	@Class2.0 // 545
	D=M // 546
	@SP // 547
	A=M // 548
	M=D // 549
	@SP // 550
	M=M+1 // 551
// C_PUSH static 1
	@Class2.1 // 552
	D=M // 553
	@SP // 554
	A=M // 555
	M=D // 556
	@SP // 557
	M=M+1 // 558
// sub
	@SP // 559
	M=M-1 // 560
	@SP // 561
	A=M // 562
	D=M // 563
	@SP // 564
	M=M-1 // 565
	@SP // 566
	A=M // 567
	M=M-D // 568
	@SP // 569
	M=M+1 // 570
// return
	@LCL // 571
	D=M // 572
	@R13 // 573
	M=D // 574
	@5 // 575
	D=D-A // 576
	A=D // 577
	D=M // 578
	@R14 // 579
	M=D // 580
	@SP // 581
	M=M-1 // 582
	A=M // 583
	D=M // 584
	@ARG // 585
	A=M // 586
	M=D // 587
	@ARG // 588
	D=M+1 // 589
	@SP // 590
	M=D // 591
	@R13 // 592
	A=M-1 // 593
	D=M // 594
	@THAT // 595
	M=D // 596
	@R2 // 597
	D=A // 598
	@R13 // 599
	A=M-D // 600
	D=M // 601
	@THIS // 602
	M=D // 603
	@R3 // 604
	D=A // 605
	@R13 // 606
	A=M-D // 607
	D=M // 608
	@ARG // 609
	M=D // 610
	@R4 // 611
	D=A // 612
	@R13 // 613
	A=M-D // 614
	D=M // 615
	@LCL // 616
	M=D // 617
	@R14 // 618
	A=M // 619
	0;JMP // 620