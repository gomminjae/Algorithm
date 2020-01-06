//
//  Queue.swift
//  Basic
//
//  Created by Apple on 2020/01/06.
//  Copyright © 2020 Apple. All rights reserved.
//
import Foundation

//기본구현
public struct Queue<T> {
    internal var data = Array<T>()
    public init(){}
    
    
    public mutating func enqueue(element: T) {
        return data.append(element)
    }
    
    public mutating func dequeue() -> T? {
        return data.removeFirst()
    }
    
    public func peek() -> T? {
        return data.first
    }
    
    public mutating func clear() {
        data.removeAll()
    }
    
    public var count: Int {
        return data.count
    }
    
    public var capacity: Int {
        get {
            return data.capacity
        }
        set {
            data.reserveCapacity(newValue)
        }
    }
    
    public func isEmpty() -> Bool {
        return data.isEmpty
    }
}

//description Protocol
extension Queue: CustomStringConvertible {
    public var description: String {
        return data.description + "의 새로운 queue"
    }
}

//Iterator

public struct QueueIterator<T>: IteratorProtocol {
    var currentElement: [T]
    
    public mutating func next() -> T? {
        if !self.currentElement.isEmpty {
            return currentElement.removeFirst()
        } else {
            return nil
        }
    }
}

extension Queue: Sequence {
    public func makeIterator() -> QueueIterator<T> {
        return QueueIterator(currentElement: self.data)
    }
}
