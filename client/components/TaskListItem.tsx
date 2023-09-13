import React from "react";
import styled from "styled-components";

import { TaskModel } from "../../api-types/models/TaskModel";

import { Icon } from "../icons/Icon";

const Container = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-self: stretch;
  user-select: none;
  border-radius: 4px;
  cursor: pointer;
  padding: 4px;

  &:hover {
    background-color: #f8f8f8;
  }
`;

const Text = styled.span`
  text-align: center;
  font-family: Comfortaa;
  font-size: 15px;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  letter-spacing: -0.333px;
`;

export interface TaskListItemProps {
  task: TaskModel;
  onToggleComplete?: () => void;
}

export const TaskListItem = ({ task, onToggleComplete }: TaskListItemProps) => {
  return (
    <>
      <Container>
        <Text>{task.name}</Text>
        <Icon
          onClick={onToggleComplete}
          type={task.completed ? "circle.checked" : "circle"}
        />
      </Container>
    </>
  );
};
