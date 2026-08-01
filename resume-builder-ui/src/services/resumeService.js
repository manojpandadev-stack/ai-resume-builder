import api from "./api";

export const getResumes = () => {
  return api.get("/api/resumes");
};

export const deleteResume = (id) => {
  return api.delete(`/api/resumes/${id}`);
};