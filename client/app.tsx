import React, { useState, useEffect } from "react";
import { GlobalStyles } from "./GlobalStyles";

import { TaskList } from "./components/TaskList";

import { OpenAPI, TasksService, Task } from "../api-types";

// TODO: fix to environment variable at build time
OpenAPI.BASE = "http://localhost:3000";

export const App = () => {
  const [tasks, setTasks] = useState<Task[] | null>(null);

  useEffect(() => {
    let cancel = false;
    TasksService.getTasks()
      .then((response) => response.tasks)
      .then((tasks) => {
        if (cancel) {
          // this is run if the data is loaded but the component has been unmounted
          return;
        }
        // this is run when the data is loaded and can be set on the component
        setTasks(tasks);
      });

    // this is run when the component unmounts
    return () => {
      cancel = true;
    };
  }, []);

  return (
    <>
      <GlobalStyles />
      {tasks === null ? "loading..." : <TaskList tasks={tasks} />}
    </>
  );
};
