//
//  InsertionSort.swift
//  treee
//
//  Created by Apple on 2020/04/26.
//  Copyright © 2020 minjae. All rights reserved.
//

import Foundation

public func InsertionSort<T: Comparable>(_ list: inout [T]) {
    if list.count <= 1 {
        return
    }
    
    for i in 1..<list.count {
        let x = list[i]
        var j = i
        while j > 0 && list[j - 1] > x {
            list[j] = list[j - 1]
            j-=1
        }
        list[j] = x
    }
}
var list = [5,4,3,2,1]
print(InsertionSort(list))
