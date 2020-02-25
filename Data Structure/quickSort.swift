//
//  main.swift
//  Quick sort
//
//  Created by Apple on 2020/02/25.
//  Copyright © 2020 Apple. All rights reserved.
//

import Foundation


func quickSort<T: Comparable>(_ arr: [T]) -> [T] {
    guard arr.count > 1 else { return arr }
    let pivot = arr[arr.count / 2]
    
    return quickSort(arr.filter{ $0 < pivot}) + [pivot] + quickSort(arr.filter { $0 > pivot})
}

let list = [10, 9, 4, 3, 6, 3, 2, 1]
print(quickSort(list))
