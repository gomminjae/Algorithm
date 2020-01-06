//
//  main.swift
//  Basic
//
//  Created by Apple on 2020/01/06.
//  Copyright © 2020 Apple. All rights reserved.

import Foundation

//기본 구현
public struct Stack<T> {
    
    //원소 선언
    private var element = [T]()
    
    //원소 삭제
    public mutating func pop() -> T? {
        return self.element.popLast()
    }
    //원소 입력
    public mutating func push(_ element: T) {
        self.element.append(element)
    }
    //젤 위의 원소 출력
    public func peek() -> T? {
        return self.element.last
    }
    
    //스택 비어있는지 확인
    public var isEmpty: Bool {
        return self.element.isEmpty
    }
    
    //원소 개수
    public var count: Int {
        return self.element.count
    }
}

//protocol
extension Stack: CustomStringConvertible, CustomDebugStringConvertible {
    
    public var description: String {
        return self.element.description
    }
    
    public var debugDescription: String {
        return self.element.debugDescription
    }
}

//Iterator
public struct ArrayIterator<T>: IteratorProtocol {
    var currentElement: [T]
    init(element: [T]) {
        self.currentElement = element
    }
    
    mutating public func next() ->T? {
        if !self.currentElement.isEmpty {
            return self.currentElement.popLast()
        }
        return nil
    }
}

extension Stack: Sequence {
    public func makeIterator() -> ArrayIterator<T> {
        return ArrayIterator<T>(element: self.element)
    }
    
    public init<S: Sequence>(_ s: S) where S.Iterator.Element == T {
        self.element = Array(s.reversed())
    }
}
