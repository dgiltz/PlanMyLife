//
//  Task.swift
//  PlanMyLife
//
//  Created by Declan Giltz on 2023-04-08.
//

import Foundation

class Task
{
    var title : String
    var details : String
    
    // Defines a Directed Acyclic Graph structure (Probably?)
    var subtasks : [Task]?
    var next : Task?
    var supertask : Task?
    
    var completed : Bool = false
    var dnd : Bool
    
    init(title : String, details : String, dnd : Bool = false)
    {
        self.title = title
        self.details = details
        self.dnd = dnd
    }
    
    func addSubtask(subtask : Task)
    {
        if var subt = self.subtasks {
            subt.append(subtask)
            
        } else {
            self.subtasks = [subtask,]
        }
        
        subtask.supertask = self
    }
    
    func addNext(newTask : Task)
    {
        if let nextTask = self.next {
            nextTask.addNext(newTask: newTask)
        } else {
            self.next = newTask
            newTask.supertask = self
        }
    }
    
    func suggestSubtasks() {
        <#code#>
    }
    
    func splitTask(into: Int) throws {
        <#code#>
    }
}

class Scheduled : Task
{
    var timeRange : DateInterval
    init(title : String, details : String, timeRange : DateInterval, dnd : Bool = false)
    {
        self.timeRange = timeRange
        super.init(title: title, details: details, dnd: dnd)
    }
    
    override func suggestSubtasks() {
        <#code#>
    }
    
    override func splitTask(into: Int) throws {
        <#code#>
    }
}

class Unscheduled : Task {
    var duration : TimeInterval?
    var startDate : Date?
    var endDate : Date?
    var priority : Int
    
    init(title : String, details : String, priority : Int = 3, dnd : Bool = false, duration : TimeInterval?,  startDate : Date?, endDate : Date?) {
        
        self.priority = priority
        
        if let start = startDate {
            self.startDate = start
        }
        
        if let dur = duration {
            self.duration = dur
        }
        
        if let end = endDate {
            self.endDate = end
        }
        
        super.init(title: title, details: details, dnd: dnd)
    }
    
    override func suggestSubtasks() {
        <#code#>
    }
    
    override func splitTask(into: Int) throws {
        <#code#>
    }
}
